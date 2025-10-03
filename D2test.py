class BankAccount:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited {amount}. New balance is {self.balance}.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
    def display(self):
        print(f"Account Number: {self.account_number}, Balance: {self.balance}")

A1 = BankAccount(1,25)
A2 = BankAccount(2,50)

A1.deposit(15)
A2.withdraw(2)

A1.display()
A2.display()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")

class Student(Person):
    def __init__(self, name, age, roll_number):
        super().__init__(name, age)
        self.roll_number = roll_number
    
    def display(self):
        print(f"Student Name: {self.name}, Age: {self.age}, Roll Number: {self.roll_number}")

p1 = Person("Alice", 30)
s1 = Student("Bob", 20, "S123")

p1.display()
s1.display()


class Animal():
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        print("Dog barks")

class Cat(Animal):
    def speak(self):
        print("Cat meows")

class Cow(Animal):
    def speak(self):
        print("Cow moos")

for animals in Animal.__subclasses__():
    obj = animals()
    obj.speak()