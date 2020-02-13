# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):

        self.name = name
        self.description = description
        self.n_to = 'Sorry there is no room north of {}'.format(self.name)
        self.s_to = 'Sorry there is no room south of {}'.format(self.name)
        self.e_to = 'Sorry there is no room east of {}'.format(self.name)
        self.w_to = 'Sorry there is no room west of {}'.format(self.name)
        self.items = items

    def search_item(self, item):
        for item_name in self.items:
            if item == item_name.name:
                return True
        return False

    def restock_item(self, item):
        self.items.append(item)

    def lose_item(self, item):
        for item_name in self.items:
            if item == item_name.name:
                return self.items.pop(self.items.index(item_name))

    def __str__(self):
        return str(self.__dict__)
