# Factory Method Pattern in Python

- The Factory Method is a creational design pattern that provides an interface for creating objects but allows subclasses to alter the type of objects that will be created.
- Instead, we define an interface (or an abstract class) for creating objects, and the subclasses decide which concrete class to instantiate.

This approach helps in encapsulation, loose coupling, and scalability of the code.


### Step 1: Create an interface (abstract class) for the product
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
```
- ABC (Abstract Base Class) is used to define a base class that cannot be instantiated.
- The speak() method is marked with @abstractmethod, meaning any subclass must implement this method.
- This ensures that all Animal objects (e.g., Dog and Cat) have a speak() method.
### Step 2: Create concrete implementations of the product
```python
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```
- We define two concrete classes, Dog and Cat, both inheriting from Animal.
- Each class provides its own implementation of speak():
    - Dog.speak() returns "Woof!"
    - Cat.speak() returns "Meow!"
- Now, we have different types of animals, but instead of directly creating their objects, we'll use the Factory Method.
### Step 3: Create the Factory Method
```python
class AnimalFactory(ABC):
    @abstractmethod
    def create_animal(self):
        pass

class DogFactory(AnimalFactory):
    def create_animal(self):
        return Dog()

class CatFactory(AnimalFactory):
    def create_animal(self):
        return Cat()
```
- AnimalFactory is another abstract class that defines the create_animal() method.
- This method will be responsible for creating instances of Animal subclasses.
- DogFactory is a concrete factory class that implements create_animal() and returns an instance of Dog.
- Similarly, CatFactory returns an instance of Cat.
- Now, instead of creating Dog or Cat objects directly, we will use their respective factories.
### Step 4: Client Code
```python
if __name__ == "__main__":
    dog_factory = DogFactory()
    cat_factory = CatFactory()
    
    dog = dog_factory.create_animal()
    cat = cat_factory.create_animal()
    
    print(dog.speak())  # Output: Woof!
    print(cat.speak())  # Output: Meow!
```
- The client code creates instances of DogFactory and CatFactory.
- It then calls the create_animal() method to get Dog and Cat objects.
- Finally, it calls speak() on the created objects, which prints: woof , Meow

##  Benefits of Using the Factory Method Pattern
✅ Encapsulation
The object creation logic is hidden inside factory classes.
The client doesn't need to know the exact class it is instantiating.
✅ Loose Coupling
The client code interacts with the factory, not the concrete classes.
If we need to add a new animal (e.g., Bird), we can do so without modifying existing code.
✅ Scalability
If we need more types of Animal, we just create a new factory without changing existing code.

##  Summary
- Factory Method allows a class to delegate the responsibility of object creation to subclasses.
- It helps in encapsulation, loose coupling, and scalability.
- Instead of using new (direct object instantiation), we use factories to create objects.
- This is useful in scenarios where object creation logic is complex, dynamic, or needs to be extended in the future.
