# Write a class to hold player information, e.g. what room they are in
# currently.
import sys

class Player:
    def __init__(self, name, current_room, items, in_treasure=False):
        self.name = name
        self.current_room = current_room
        self.in_treasure = in_treasure
        self.items = items


    def __str__(self):
        return f"          \nWelcome {self.name}, Please take a look around. You're currently in {self.current_room.name}, {self.current_room.description}."
    def printitems(self):
        for item in self.items:
            return item
    def getItem(self):
        selection = sys.argv[1]
        self.items.append(selection)
    def dropItem(self):
        selection = sys.argv[1]
        self.items.remove(selection)
        self.current_room.items.append(selection)
