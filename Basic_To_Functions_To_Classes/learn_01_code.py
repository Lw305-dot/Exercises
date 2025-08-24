#VARIABLES & DATA TYPES
name="Alice"
age=25
height=5.8
is_student= True

print("Name:", name)
print("Age:", age)
print("Student?", is_student)

# ✅ INPUT / OUTPUT
# Uncomment to try!
# user_name = input("Enter your name: ")
# print(f"Hello, {user_name}!")

# ✅ IF-ELSE
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# ✅ LOOPS
# For loop
for i in range(1, 6):
    print("Counting:", i)

# While loop
count = 1
while count <= 3:
    print("While loop:", count)
    count += 1

# ✅ FUNCTIONS
def greet(name):
    return f"Hello, {name}!"

print(greet("Bob"))

def add(a, b):
    return a + b

print("Addition:", add(3, 4))

# ✅ FUNCTION WITH DEFAULT ARGUMENTS
def power(base, exponent=2):
    return base ** exponent

print("Power:", power(3))
print("Power with exponent:", power(2, 5))

# ✅ CLASSES & OBJECTS
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, and I'm {self.age} years old.")

# Creating an object
person1 = Person("Charlie", 30)
person1.introduce()