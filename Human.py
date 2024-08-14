class Human:
    def _init_(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def intro(self):
        print(f"  My Name is: {self.name}, and  I am {self.age}.")


    def eat(self, eat):
        print(f"{self.name} eat {eat}")