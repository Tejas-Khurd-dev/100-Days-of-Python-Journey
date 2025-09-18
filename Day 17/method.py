class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} Woof!")

dog1 = Dog("Tommy")
dog2 = Dog("Bruno")

dog1.speak()
dog2.speak()
