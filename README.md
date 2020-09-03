## OBJECT ORIENTED PROGRAMMING (OOP)
Object Oriented programming (OOP) is a programming pattern that includes or relies on the concept of classes and objects. It is used to structure a software program into simple, reusable pieces of code blueprints (usually called classes) which are used to create individual instances of objects.  

**e.g.**  

```python
class introduction:

    # declairing variables (NOTE: variables definied here can be called even outside the class)
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

As you can see in the above example we made a class `introduction` with some methods. Now we need to think that example in a wider level. Suppose that code is being used in a company and we need to print name and age of 100s of employees, we have already created a plueprint of the print statements and now we just need to make an instance and call the methods of the class for different employees with their names and age as parameters,  
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

**Now this may seem like a lot of work just to print names and ages and many of you might be thinking why not print the names and ages directly using the predefined function `print()`. Well you may be right in this case but classes are gonna be a lot more useful in large scale programming. So the best way of learning at start is try to accept the concepts without overthinking it.**

## Why OOP?
OOP makes code organized, reusable, and easy to maintain.  
Benefits of OOP include security: OOP prevents unwanted access to data, or exposing proprietary code through encapsulation and abstraction.  

Now let's take a look at all the aspects more closely:

#### ORGANISED:
In python we declair veriables and perform actions on those veriables with the help of functions. Now when you work will large number of variables and functions (performing actions on those functions) wouldn't it be good if we can find all the variables and functions associated with them in the same place (for the perpose of debugging or altering the program later for some reason). This is where OOP comes into use, we can bundle the variables and functions associated with them in different classes.  
We can aslo call the objects of the class at any moment in our code.  
In the above example we bundles the variables for introduction and actions on those variables (print_name and print_age) under the class `introduction`.  

#### REUSABLE:
In OOP reusability means we can use the objects of a class into another class(subclass). i.e. we can use all the objects of a class without writting the code again and again, plus we can add more objects to the subclass. This way the subclass will have the properties of both the parent class and the subclass. This whole mechanism is called `inheritance`.  
Refer the inheritance topic for more details.  

**e.g.**  
```python
class employee_name:         # parent class
    name = ""

    def print_name(self, name):
        print("My name is {}".format(name))

class introduction(employee_name):        # subclass
    age = 0

    def print_age(self, age):
        print("I am {} years old".format(age))

intro = introduction()

intro.print_name("Amit")
intro.print_age(20)
```
**OUTPUT:**  
```
My name is Amit
I am 20 years old
```
Here the subclass `introduction` inherits the parent class `employee_name`, in this way we are reusing the parent class in our subclass without writing the  parent class codes again. This gives all the features of the parent class to the sub class plus additional features(print_age) of the sub class. Now we create the instance of the sub class, using the instant of the sub class we can call the objects of the parent class as well.

#### Easy to maintain:
It is easy to maintain as if you want some changes to the properties of the class, you can simply go change/alter the class. This will automatically change the property in all the places you used the class instant or called a class object.

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

**e.g.**  

```python
class introduction:

    # declairing variables (NOTE: variables definied here can be called even outside the class)
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

print(intro.age) 
```
here,  
class: `introduction`  
Object: `intro`  
Methods: all the functions, `print_name` and `print_age`  
Attributes: declared variables, `name` and `age`  

## `self` and `__init__` methods:
First let's look at the book definition of these methods,  

**self:**  
self represents the instance of the class. By using the "self" keyword we can access the attributes and methods of the class in python.  

**\__init__:**  
`__init__` is a predefined method in python OOP. It is known as a constructor in object oriented concepts. This method called when an object is created from the class and it allow the class to initialize the attributes of a class.  

Now lets understand what it is,  
You have seen the above example of the class `introduction`. We also created an instance for the class,
```python
intro = introduction()
```
This is alright but won't it be interesting if we can pass the parameters at the same time we create the instance,
```python
intro = introduction("Amit", 20)
```
This is where `__init__` comes into play, it is a predefined method which gets called automatically when we create the instance of a class.  
Let's see an example and understand more,  
```python
class introduction:
    def __init__(self, name, age):
        self.n = name
        self.a = age

    def print_name(self):
        print("My name is {}".format(self.n))

    def print_age(self):
        print("I am {} years old".format(self.a))

intro = introduction("Amit", 20)

intro.print_name()
intro.print_age()
```
**OUTPUT:**  
```
My name is Amit
I am 20 years old
```
You might be thinking why haven't i passed any parameter for `self`, well because it automatically takes the instance(intro) as its parameter. 
In the example `self` will take `intro` as its parameter,    
`self.n = name` will represent `intro.a = name` and `self.a = age` will represent `intro.a = age`.  

When we create the instance, the `__init__` method will be called automatically initializing everything inside it. The parameters `Amit` and `20` gets passed to the `__init__` method as arguments, and the `__init__` method will assign the parameters to the variables `self.n`(intro.n) and `self.a`(intro.a) respectively which can be used by the methods of the class.  

### Why do we use `__init__`?
When a new instance of a python class is created, it is the __init__ method which is called and proves to be a very good place where we can modify the object after it has been created. Means we don't need locate the methods called in different parts of the program. We can just alter the parameters in the object(instance).  
e.g.
```python
intro = introduction("Sumit", 18)
```
**OUTPUT**  
```
My name is Sumit
I am 18 years old
```
Here we didn't need to find the called methods("print_name" and "print_age"). We just went to the instance and altered the name and age from there. Isn't it convenient to have `__init__` in our class. It gets more convenient when we have a lot of methods in our class. It saves us time to find every called method of the class and alter their parameters one by one.  

Now that's done, how can we just blindly believe the statement `"__init__ function gets called automatically when the instance is created"`. The answer is simple, let's just see an example.  
e.g.  
```python
class introduction:
    def __init__(self, name, age):
        self.n = name
        self.a = age

        print("My name is {}".format(self.n))

        print("I am {} years old".format(self.a))

intro = introduction("Amit", 20)
```
**OUTPUT:**  
```
My name is Amit
I am 20 years old
```

## Four principles of OOP:

#### 1. Inheritance

Inheritance allows classes to inherit features of other classes. Put another way, parent classes extend attributes and behaviors to child classes.  
Inheritance supports reusability – if basic attributes and behaviors are defined in a parent class, child classes can be created extending the functionality of the parent class, and adding additional attributes and behaviors.  

In simple words inheritance is a way of creating a new class for using details of an existing class without modifying it. The newly formed class is a derived class (or child class). Similarly, the existing class is a base class (or parent class).  
[Link to the example](https://github.com/amitkumarsaw/Object-Oriented-Programming-OOP/blob/master/inheritance.py)

#### 2. Encapsulation
Using OOP in Python, we can restrict access to methods and variables. This prevents data from direct modification which is called encapsulation.
Encapsulation hides the internal software code implementation inside a class, and hides internal data of inside objects.  
[Link to the example](https://github.com/amitkumarsaw/Object-Oriented-Programming-OOP/blob/master/encapsulation.py)

#### 3. Abstraction
Abstraction means that the user interacts with only selected attributes and methods of an object. Abstraction uses simplified, high level tools, to access a complex object.  
Abstraction is using simple classes to represent complexity. Abstraction is an extension of encapsulation.  
[Link to the example](https://github.com/amitkumarsaw/Object-Oriented-Programming-OOP/blob/master/abstraction.py)

#### 4. Polymorphism
Polymorphism is designing objects to share behaviors. Using inheritance, objects can override shared parent behaviors, with specific child behaviors.  
Polymorphism allows the same method to execute different behaviors in two ways: method overriding and method overloading.

In simple words polymorphism is an ability (in OOP) to use a common interface for multiple forms (data types).  
[Link to the example](https://github.com/amitkumarsaw/Object-Oriented-Programming-OOP/blob/master/polymorphism.py)
