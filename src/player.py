# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, current_room):

        self.name = name
        self.current_room = current_room
        self.items = []

    def search_inventory(self, item):
        for item_name in self.items:
            if item == item_name.name:
                return True
        return False

    def drop_item(self, item):
        for item_name in self.items:
            if item == item_name.name:
                return self.items.pop(self.items.index(item_name))

    def pickup_item(self, item):

        self.items.append(item)

    def __str__(self):
        return str(self.__dict__)
