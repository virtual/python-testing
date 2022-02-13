class Phonebook():
    def __init__(self):
        self.phonebook = {}

    def add(self, name, number):
        self.phonebook[name] = number

    def lookup(self, name):
        return self.phonebook[name]

    def is_consistent(self):
        for name in self.phonebook:
            if self.phonebook[name] != self.lookup(name):
                return False
        return True