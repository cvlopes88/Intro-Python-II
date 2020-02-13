from room import Room
from player import Player
from item import Item
import textwrap


# Declaring all items:
items = {
    'gold': Item('gold', 'gold is the only way to trade'),
    'shield': Item('shield', 'protetion'),
    'food': Item('food', 'for when they are hungry')
}

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",
                     [items['gold'], items['food']]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", []),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [items['shield']]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [items['food']]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.


def print_items(item_array):

    if len(item_array) > 0:
        print('Items in the Room:')
        for item in item_array:
            print(item)
    else:
        print('No items in Room.')


#enter your name here
player_name = input('Before you proceed, please type in a name for your player! ')


# Initial room variable:
current_room = room['outside']


# initializes the Player class with user inputted name and initial room (cave entrance)
character = Player(player_name, room['outside'])

while True:

    print(
        f'\nCurrent room: name {current_room.name}, description {current_room.description}\n')

    print_items(current_room.items)

    user_input = input(
        'Please enter a direction you want the player to move. Selections include: [n, s, e, w]! ')

    user_input = user_input.split(' ')

    if len(user_input) == 1:

        if user_input[0] == 'n':

            if not isinstance(current_room.n_to, str):
                current_room = current_room.n_to
                character.current_room = current_room
            else:
                print(current_room.n_to)

        elif user_input[0] == 's':

            if not isinstance(current_room.s_to, str):
                current_room = current_room.s_to
                character.current_room = current_room
            else:
                print(current_room.s_to)

        elif user_input[0] == 'e':

            if not isinstance(current_room.e_to, str):
                current_room = current_room.e_to
                character.current_room = current_room
            else:
                print(current_room.e_to)

        elif user_input[0] == 'w':

            if not isinstance(current_room.w_to, str):
                current_room = current_room.w_to
                character.current_room = current_room
            else:
                print(current_room.w_to)

        elif user_input[0] == 'i' or user_input[0] == 'inventory':

            print('Character\'s item inventory: ')
            for item in character.items:
                print(item)

        elif user_input[0] == 'q':
            print('see you soon!!!')
            break

        else:

            print(
                'Please use the valid inputs [n, s, e, w] to move or q to quit')

    elif len(user_input) == 2:

        if user_input[0] == 'take':

            if current_room.search_item(user_input[1]):

                acquired_item = current_room.lose_item(user_input[1])
                acquired_item.on_take()
                character.pickup_item(acquired_item)

            else:

                print(
                    f'Can\'t find item {user_input[1]} in room {current_room.name}')

        elif user_input[0] == 'drop':

            if character.search_inventory(user_input[1]):

                reclaim_item = character.drop_item(user_input[1])

                current_room.restock_item(reclaim_item)

            else:

                print(f'Can\'t find item {user_input[1]} in inventory')

        else:

            print(
                'Please use the valid inputs [n, s, e, w] to move, drop and take for items, or q to quit')
