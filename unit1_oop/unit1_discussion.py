"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""


from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    class ParentClass:
    species = "Generic Entity"  # class variable

    def __init__(self, name, age):
        self.name = name          # instance variable
        self.age = age            # instance variable

    def describe(self):
        return f"ParentClass Object → Name: {self.name}, Age: {self.age}, Species: {self.species}"


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    category = "Child Type"  # new class variable

    def __init__(self, name, age, hobby, grade):
        super().__init__(name, age)  # inherit parent attributes
        self.hobby = hobby           # new instance variable
        self.grade = grade           # new instance variable

    def describe(self):  # override parent method
        return (f"ChildClass Object → Name: {self.name}, Age: {self.age}, "
                f"Hobby: {self.hobby}, Grade: {self.grade}, Category: {self.category}")

    def child_method(self):
        return f"{self.name} enjoys {self.hobby} and is in grade {self.grade}."


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    obj1 = ChildClass("Alex", 12, "Drawing", "7th")
    obj2 = ChildClass("Jordan", 13, "Coding", "8th")

    print("\nAccess class variable through class:", ChildClass.category)
    print("Access class variable through object:", obj1.category)

    obj1.unique_trait = "Creative"  # add attribute only to obj1

    print("\nObject 1 namespace:", obj1.__dict__)
    print("Object 2 namespace:", obj2.__dict__)

    print("\nClass namespace:", ChildClass.__dict__)


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = {
        "name": "NestedObject",
        "data": [1, 2, [3, 4]]
    }

    shallow = copy(original)
    deep = deepcopy(original)

    original["data"][2].append(5)

    print("\nOriginal:", original)
    print("Shallow Copy:", shallow)
    print("Deep Copy:", deep)

    # Shallow copy → nested objects are shared
    # Deep copy → nested objects are fully duplicated


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    parent = ParentClass("Morgan", 40)
    print("\nParent Object Test:")
    print(parent.describe())

    child = ChildClass("Taylor", 15, "Basketball", "9th")
    print("\nChild Object Test:")
    print(child.describe())
    print(child.child_method())

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()