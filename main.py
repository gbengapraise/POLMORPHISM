class Dog:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("I an walk")

class Snake:
    def __init__(self, name):
        self.name = name

    def move(self):
        print("I can slither")


charles = Dog("charles")
mamber = Snake("mamber")


animals = (charles, mamber)

for animal in animals:
    animal.move()
