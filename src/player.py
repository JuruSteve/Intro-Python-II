# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room):
        self.name = name
        self.current_room = room

    def __str__(self):
        s = f"({self.name})"
        return s

    def __repr__(self):
        r = f"(Player({repr(self.name)}, {repr(self.current_room)}))"
        return r

    def getName(self):
        s = f"{self.name}"
        return s

    def getCurrentRoom(self):
        s = f"{self.current_room}"
        return s
