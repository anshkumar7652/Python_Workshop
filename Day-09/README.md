# Day 09 - Object-Oriented Programming Fundamentals

## Topics Covered

Today focused on the fundamentals of Object-Oriented Programming (OOP) in Python, including:

- Classes and Objects
- Class Variables (Static Variables)
- Instance Variables
- Constructors (`__init__`)
- Constructor Overloading Behavior in Python
- Public, Protected, and Private Members
- Name Mangling
- Static Variables vs Global Variables

---

## Files Overview

### 1. class_variables_basic.py
Demonstrates:
- Class creation
- Class variable declaration
- Accessing class variables using the class name

Concepts:
- Class Variables
- Class Scope

---

### 2. class_and_instance_variables.py
Demonstrates:
- Difference between class variables and instance variables
- Constructor usage
- Accessing variables through objects and class names

Concepts:
- Instance Variables
- Class Variables
- Object Creation

---

### 3. constructor_overloading_demo.py
Demonstrates:
- Multiple constructors in Python
- Why Python does not support constructor overloading
- Constructor overriding behavior

Concepts:
- Constructors
- Local Variables
- Method Calls

Key Observation:
- When multiple constructors are defined, the last constructor replaces the previous one.

---

### 4. protected_members_demo.py
Demonstrates:
- Protected members using a single underscore (`_`)
- Accessing protected attributes outside the class

Concepts:
- Protected Variables
- Naming Conventions

Key Observation:
- Protected members are accessible outside the class but should be treated as internal.

---

### 5. private_members_demo.py
Demonstrates:
- Private variables using double underscores (`__`)
- Accessing private members through class methods

Concepts:
- Private Variables
- Encapsulation

Key Observation:
- Private variables cannot be accessed directly from outside the class.

---

### 6. name_mangling_demo.py
Demonstrates:
- Python Name Mangling
- Internal renaming of private variables
- Using `__dict__` to inspect object attributes

Concepts:
- Name Mangling
- Object Internals
- Special Attributes

---

### 7. static_vs_global_variables.py
Demonstrates:
- Difference between global variables and class variables
- Static variable behavior
- Updating class variables

Concepts:
- Global Variables
- Static Variables
- Class Attributes

---

### 8. private_class_variables.py
Demonstrates:
- Private class variables
- Accessing mangled class variables
- Class-level encapsulation

Concepts:
- Private Class Variables
- Name Mangling

---

## Key Learnings

- Class variables are shared by all objects.
- Instance variables belong to individual objects.
- Python does not support traditional constructor overloading.
- Protected members use a single underscore (`_`).
- Private members use double underscores (`__`).
- Python implements privacy using name mangling.
- Static variables belong to the class rather than individual objects.
- Global variables and static variables serve different purposes.

---

## Outcome

By the end of Day 09, I gained a strong understanding of how Python classes manage data, how access modifiers work, and how Python implements encapsulation through naming conventions and name mangling.