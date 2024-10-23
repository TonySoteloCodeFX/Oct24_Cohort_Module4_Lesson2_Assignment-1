<h1>Assignment: OOP Fundamentals</h1>
<hr>

<h3>1. City Infrastructure Management System</h3>

<b><i>Objective:</i></b> The aim of this assignment is to apply the concepts of Object-Oriented Programming in Python to build a simulated City Infrastructure Management System. This system will incorporate classes, objects, methods, and data structures to manage different aspects of a city, such as buildings, traffic, and events.

<h5>Task 1: Vehicle Registration System</h5>

<b><i>Problem Statement:</i></b> Create a Python class Vehicle with attributes registration_number, type, and owner. Implement a method update_owner to change the vehicle's owner. Then, create a few instances of Vehicle and demonstrate changing the owner.

<b><i>Code Example:</i></b> Provide a basic structure for the Vehicle class without methods.

```
    class Vehicle:
        def __init__(self, reg_num, type, owner):
            self.registration_number = reg_num
            self.type = type
            self.owner = owner
```
<b><i>Expected Outcome:</i></b> Completion of the Vehicle class with the update_ownermethod and a demonstration script showing the creation of Vehicle objects and updating their owners.
<hr>

<h5>Task 2: Event Management System Enhancement</h5>

<b><i>Problem Statement:</i></b> Extend an existing Event class by adding a feature to keep track of the number of participants. Implement a method add_participant that increases the count and a method get_participant_count to retrieve the current count.

<b><i>Code Example:</i></b> Basic Event class without participant tracking.

```
    class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
```
<b><i>NOTE:</i></b> Ensure that all code in your file is ready to run. This means that if someone opens your file and clicks the run button at the top, all code executes as intended. For example, if there are if statements, print statements, or for loops, they should function correctly and display output in the console as expected. If you have a function, make sure the function is called and runs. If there are classes/objects, make sure they are instantiated and the methods are called.

The goal of this note is to ensure that all code in your Python file runs smoothly and that is has been tested.