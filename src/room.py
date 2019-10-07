# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        """"Constructor"""
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        s = f"Room({self.name})"
        return s

    def __repr__(self):
        r = f"(Room({repr(self.name)}, {repr(self.description)}))"
        return r

    def getName(self):
        s = f"{self.name}"
        return s

    def getDescription(self):
        s = f"{self.description}"
        return s
