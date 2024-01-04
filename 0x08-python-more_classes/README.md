this directory holds files for;
What is a Class
A class is a blueprint for creating objects. It defines the structure and behavior that its instances will have.

Objects and Instances
An object is an instance of a class. It represents a unique entity with attributes and behaviors defined by the class.

Difference between Class and Object/Instance
A class is a template for creating objects, while an object is a specific instance of a class.

Attributes
Attributes are the properties or characteristics of an object.

Public, Protected, and Private Attributes
Attributes can be public, protected, or private, defining their accessibility.

Self
self is a reference to the instance of the class. It allows access to instance attributes and methods.

Methods
Methods are functions defined within a class and operate on its instances.

Special __init__ Method
__init__ is a special method used for initializing object attributes when an instance is created.

Data Abstraction, Data Encapsulation, and Information Hiding
These concepts involve hiding implementation details and exposing only necessary information.

Property
A property is a special attribute that allows controlled access to an object's attributes.

Difference between Attribute and Property in Python
Attributes are raw data, while properties provide controlled access with getter and setter methods.

Pythonic Way to Write Getters and Setters
Use the @property, @<attribute>.setter, and @<attribute>.deleter decorators for cleaner getter and setter methods.

Special __str__ and __repr__ Methods
__str__ and __repr__ methods control the string representation of an object.

Difference between __str__ and __repr__
__str__ is for a user-friendly representation, while __repr__ is for a developer-friendly, unambiguous representation.

Class Attribute
A class attribute is shared among all instances of a class.

Difference between Object Attribute and Class Attribute
Object attributes are specific to an instance, while class attributes are shared among all instances.

Class Method
A class method is a method that is bound to the class and not the instance.

Static Method
A static method is a method that is bound to the class and not the instance, without access to instance-specific data.

Dynamically Creating Arbitrary New Attributes
Python allows dynamic creation of new attributes during runtime.

Binding Attributes to Objects and Classes
Attributes can be bound to both instances and the class itself.

__dict__ of a Class and an Instance
__dict__ is a dictionary containing a class or an instance's attributes.

How Does Python Find the Attributes of an Object or Class
Python uses a specific attribute lookup order to find attributes in objects and classes.

How to Use the getattr Function
The getattr function allows you to access an attribute using its name dynamically.