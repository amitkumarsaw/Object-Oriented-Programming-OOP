## OBJECT ORIENTED PROGRAMMING (OOP)
Object Oriented programming (OOP) is a programming pattern that includes or relies on the concept of classes and objects. It is used to structure a software program into simple, reusable pieces of code blueprints (usually called classes) which are used to create individual instances of objects.  

**e.g.**  

```python
class introduction:

    # defining variables (NOTE: variables definied here can be called even outside the class)
    name = ""
    age = 0

    # functions inside a class are called METHODS
    def print_name(self, name):
        print("My name is {}".format(name))

    def print_age(self, age):
        print("I am {} years old".format(age))

intro = introduction()                # creating instance

# calling methods and variables with the help of instances
intro.print_name("Amit")                                    # the "self" argument given in the methods will automatically take "intro" as its value
intro.print_age(20)

print(intro.age)                                           # calling variable outside the class
```
**OUTPUT:**  
```
My name is Amit
I am 20 years old
0
```
You must have heard the word `PLUEPRINT` while studying classes, let's what it is with the help of above example,  

As you can see in the above example we made a class `introduction` with some methods. Now we need to think that example in a wwider way. Suppose that code is being used in a company and we need to print name and age of 100s of employees, we have already created a plueprint of the print statements and now we just need to make an instance and call the methods of the class for different employees with their names and age as parameters,  
```python
intro.print_name("Amit")
intro.print_age(20)

print("\n")                      # to give a line space
intro.print_name("Sumit")
intro.print_age(19)

print("\n")
intro.print_name("Raj")
intro.print_age(25)
```
**OUTPUT:**  
```
My name is Amit
I am 20 years old

My name is Sumit
I am 19 years old

My name is Raj
I am 25 years old
```
This is also a reason why we use OOP.  

**Now this may seem like a lot of work just to print names and ages and many of you might be thinking why not print the names and ages directly using the predefined function `print()`. Well you may be right in this case but classes are gonna be a lot more useful in large scale programming. So just try to accept the concepts without overthinking it**

## Why OOP?
OOP makes code organized, reusable, and easy to maintain.  
Benefits of OOP include security: OOP prevents unwanted access to data, or exposing proprietary code through encapsulation and abstraction.  



### Building blocks of OOP :
- classes
- objects
- methods
- attributes

#### Classes :
In a nutshell, they’re essentially user defined data types. Classes are where the programmer creates a blueprint for the structure of methods and attributes.  
Individual objects are instantiated, or created from this blueprint.

#### Objects :
Objects are instances of classes created with specific data.

#### Attributes :
Attributes are the information that is stored. Attributes are defined in the Class template. When objects are instantiated individual objects contain data stored in the Attributes field. The state of an object is defined by the data in the object’s attributes fields.

#### Methods
Methods represent behaviors. Methods perform actions; methods might return information about an object, or update an object’s data.  
The method’s code is defined in the class definition. When individual objects are instantiated, these objects can call the methods defined in the class.

## Four principles of OOP:

#### 1. Inheritance

Inheritance allows classes to inherit features of other classes. Put another way, parent classes extend attributes and behaviors to child classes.  
Inheritance supports reusability – if basic attributes and behaviors are defined in a parent class, child classes can be created extending the functionality of the parent class, and adding additional attributes and behaviors.  

In simple words inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).

#### 2. Encapsulation
Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation.
Encapsulation hides the internal software code implementation inside a class, and hides internal data of inside objects.

#### 3. Abstraction
Abstraction means that the user interacts with only selected attributes and methods of an object. Abstraction uses simplified, high level tools, to access a complex object.  
Abstraction is using simple classes to represent complexity. Abstraction is an extension of encapsulation.

#### 4. Polymorphism
Polymorphism is designing objects to share behaviors. Using inheritance, objects can override shared parent behaviors, with specific child behaviors.  
Polymorphism allows the same method to execute different behaviors in two ways: method overriding and method overloading.

In simple words polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).
