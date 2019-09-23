class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof!")

my_dog = Dog("Paris","German Shepard")

print(my_dog)
print(my_dog.name, my_dog.breed)
my_dog.bark()
