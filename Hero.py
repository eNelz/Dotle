class Hero:
    def __init__(self, name, attr, range):
        self.name = name
        self.attr = attr
        self.range = range

    def printName(self):
        print(self.name)