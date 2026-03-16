# Lab 7 – Introduction to Python (OOP)

## Task 2: Object-Oriented Programming in Python

This project demonstrates basic Object-Oriented Programming (OOP) concepts using Python.

### Base Class
- **Animal**
  - Attributes: `name`, `age`, `weight`
  - Methods: `speak()`, `describe()`
  - Special method: `__str__()` for string representation

### Child Classes
- **Dog**
  - Inherits from `Animal`
  - Additional attribute: `breed`
  - Overrides `speak()` method
  - Unique method: `fetch()`

- **Cat**
  - Inherits from `Animal`
  - Additional attribute: `indoor`
  - Overrides `speak()` method
  - Unique method: `purr()`

### Concepts Demonstrated
- Classes and objects
- Inheritance
- Method overriding
- Polymorphism
- Using modules and imports

### Files
- `models.py` – contains the class definitions
- `main.py` – creates objects and demonstrates their behavior

### Example Features
- Creating multiple animals (dogs and cats)
- Storing objects in a list
- Iterating over objects
- Demonstrating polymorphism with the `speak()` method
- Calling class-specific methods (`fetch()`, `purr()`)