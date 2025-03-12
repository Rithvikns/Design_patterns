# Factory Method Pattern in Python

## The Factory Method is a creational design pattern that provides an interface for creating objects
## but allows subclasses to alter the type of objects that will be created.

### Step 1: Create an interface (abstract class) for the product
```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass
```
### Step 2: Create concrete implementations of the product
```python
class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"
```
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
