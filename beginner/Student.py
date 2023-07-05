class Student:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def toString(self):
        print(self.name + " - " + self.id)
