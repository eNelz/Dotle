class Hero:
    def __init__(self, name, attr, range, ms):
        self.name = name
        self.attr = attr
        self.range = range
        self.ms = ms

    def printName(self):
        print(self.name)