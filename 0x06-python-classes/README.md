Python - Classes and Objects


Class:
A class in Python is a blueprint for creating objects. It defines a data structure that encapsulates data and the methods that operate on that data.

Object and Instance:
An object is an instance of a class. An instance is a specific realization of any object. In other words, a class is like a blueprint, and an object is an instance of that blueprint.

Difference between Class and Object/Instance:
Class: A template or blueprint that defines attributes and behaviors common to all objects of the class.
Object/Instance: A specific instantiation of a class with actual values.
Attribute:
An attribute is a characteristic of an object. It represents some property or piece of data associated with the object.

Public, Protected, and Private Attributes:
Public: Accessible from outside the class.
Protected: Accessible within the class and its subclasses.
Private: Accessible only within the class.
self:
self is a convention in Python to represent the instance of the class. It is the first parameter of any instance method in a class.

Method:
A method is a function associated with an object. In Python, it is called on an instance of a class.

__init__ Method:
It is a special method in Python classes that is called when an object is created. It is used to initialize object attributes.

Data Abstraction, Data Encapsulation, and Information Hiding:
Data Abstraction: Presenting only essential features of an object, hiding the unnecessary details.
Data Encapsulation: Bundling data and methods that operate on the data into a single unit (class).
Information Hiding: Restricting access to certain details of an object and exposing only what is necessary.
Property:
A property is a special kind of attribute managed by getter, setter, and deleter methods.

Attribute vs. Property in Python:
An attribute is a variable within a class, while a property has getter, setter, and deleter methods associated with it.

Pythonic way to write getters and setters:
Use the @property, @<attribute>.setter, and @<attribute>.deleter decorators.

Dynamically create arbitrary new attributes:
Use the setattr(obj, 'attribute_name', value) function.

Bind attributes to objects and classes:
Attributes can be bound to objects dynamically. For classes, they are typically defined in the class body.

__dict__:
__dict__ is a dictionary containing a class or instance's attributes.

Finding attributes in Python:
Python looks for attributes in the instance's dictionary, then in the class, and finally in the base classes.

getattr function:
getattr(obj, 'attribute_name') is used to get the value of an attribute.