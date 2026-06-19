# Day 10 – Inheritance, Polymorphism and Advanced OOP

## Overview

Today's session expanded on the OOP concepts introduced on Day 9. I explored how classes can inherit features from other classes, how Python supports polymorphism, and how special methods can be used to customize the behavior of objects.

The exercises also included practical problems involving recursion, factorials, Fibonacci series, and utility programs implemented using classes.

---

## Topics Covered

* Magic Methods
* Operator Overloading
* Single Inheritance
* Multilevel Inheritance
* Constructor Chaining
* Method Overriding
* Polymorphism
* Abstract Classes
* Recursion
* OOP-Based Problem Solving

---

## Programs

### magic_methods_demo.py

A simple demonstration showing that operators in Python are internally implemented through special (magic) methods such as `__add__()`.

**Concepts Practiced**

* Magic Methods
* Internal Working of Operators

---

### operator_overloading_mass.py

Created a custom `mass` class and overloaded the `+` operator so that two mass objects can be added together naturally.

**Concepts Practiced**

* Operator Overloading
* `__add__()`
* `__repr__()`

---

### prime_factorials.py

Finds all prime numbers up to a given number and stores the factorial of each prime number in a list.

**Concepts Practiced**

* Prime Number Checking
* Recursion
* Class-Based Programming

---

### single_inheritance_demo.py

A basic example of inheritance where a child class inherits methods from a parent class.

**Concepts Practiced**

* Single Inheritance
* Code Reusability

---

### multilevel_inheritance_demo.py

Demonstrates inheritance across multiple levels of classes.

**Concepts Practiced**

* Multilevel Inheritance
* Parent-Child Relationships

---

### constructor_chaining_demo.py

Shows how constructors of parent classes can be invoked from child classes using `super()`.

**Concepts Practiced**

* Constructor Chaining
* Parent Constructor Invocation

---

### student_information_system.py

A simple student information program that stores and displays student details using a class.

**Concepts Practiced**

* Instance Variables
* User Input
* Object Methods

---

### vehicle_inheritance_demo.py

Demonstrates inheritance using vehicle-related classes.

**Concepts Practiced**

* Inheritance
* Method Sharing

---

### factorial_fibonacci_generator.py

Calculates the factorial of a number and then generates a Fibonacci sequence based on the result.

**Concepts Practiced**

* Recursion
* Fibonacci Series
* Method Calls

---

### method_overriding_demo.py

Shows how a child class can redefine a method inherited from its parent class.

**Concepts Practiced**

* Method Overriding
* Polymorphism
* `super()`

---

### abstract_classes_demo.py

Introduces abstract classes and abstract methods using Python's `abc` module.

**Concepts Practiced**

* Abstraction
* Abstract Base Classes (ABC)
* Interfaces

---

### oop_utility_program.py

A collection of utility methods for:

* Even/Odd checking
* Factorial calculation
* Prime number testing
* Finding the greatest of three numbers
* Extracting vowels from a string

**Concepts Practiced**

* Method Organization
* Reusable Class Design

---

## Key Takeaways

* Inheritance allows child classes to reuse code from parent classes.
* Constructors can be chained using `super()`.
* Operator overloading makes custom objects behave like built-in data types.
* Method overriding enables polymorphic behavior.
* Abstract classes help define a common structure for related classes.
* OOP makes programs more organized, reusable, and easier to maintain.

---

## Reflection

Day 10 was an important step in understanding advanced Object-Oriented Programming concepts. The exercises showed how Python supports inheritance, polymorphism, abstraction, and operator overloading, which are widely used in real-world software development.
