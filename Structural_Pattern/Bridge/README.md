# Bridge Pattern

## Introduction
The **Bridge Pattern** is a structural design pattern that helps decouple an abstraction from its implementation, allowing both to evolve independently. Instead of using inheritance, it relies on composition, enabling greater flexibility and scalability in system design.

## Problem Statement
When designing complex systems, we often encounter multiple orthogonal dimensions of change. If we use inheritance to model these variations, we end up with a **Cartesian explosion** of subclasses. This makes the code hard to maintain and extend.

### Example Problem
Imagine we are designing a system for rendering shapes with different drawing APIs (e.g., vector and raster). Using inheritance alone, we might define classes as follows:

```
Shape (abstract)
├── Circle
│   ├── VectorCircle
│   ├── RasterCircle
└── Square
    ├── VectorSquare
    ├── RasterSquare
```

As more shapes and rendering methods are added, the number of classes grows exponentially.

## Solution: Bridge Pattern
The **Bridge Pattern** addresses this issue by extracting one of the varying dimensions into a separate hierarchy and using composition instead of inheritance.

### Structure
The pattern consists of:
1. **Abstraction**: Defines a high-level control interface and maintains a reference to an Implementor.
2. **Refined Abstraction**: Extends the abstraction but delegates work to the Implementor.
3. **Implementor**: Defines the interface for implementation classes.
4. **Concrete Implementor**: Implements the Implementor interface.

### UML Diagram
```
        Abstraction
            |
   -----------------
   |               |
Refined Abstraction    Implementor
                      |
                      Concrete Implementor
```
# Abstract Method 
The @abstractmethod decorator in Python is used to define an abstract method inside an abstract base class (ABC).

Key Points:
It enforces that any subclass must implement the method.
It prevents instances of the abstract class from being created.
It promotes consistency across subclasses.

## Example 
```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Animal(ABC):
    
    @abstractmethod
    def make_sound(self):
        """This method must be implemented by subclasses."""
        pass

# Concrete Subclass
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# dog = Animal()  # ❌ ERROR: Cannot instantiate abstract class
dog = Dog()  # ✅ Works fine
print(dog.make_sound())  # Output: Woof!

```
### How It Works
- ABC (Abstract Base Class): The Animal class inherits from ABC, making it an abstract class.
- @abstractmethod: The make_sound method is defined but not implemented in Animal, forcing subclasses to provide their own implementation.
- Instantiation Restriction: If you try to instantiate Animal directly, Python will raise an error.
Why Use @abstractmethod?
✅ Ensures subclasses implement necessary methods.
✅ Provides a blueprint for derived classes.
✅ Helps in maintaining a clean, structured design.

## Implementation in Python

### Example 1: Shape Rendering
```python
from abc import ABC, abstractmethod

# Implementor
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass

# Concrete Implementors
class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing a circle with radius {radius} using vector rendering")

class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for a circle with radius {radius}")

# Abstraction
class Shape(ABC):
    def __init__(self, renderer: Renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

# Refined Abstraction
class Circle(Shape):
    def __init__(self, renderer: Renderer, radius):
        super().__init__(renderer)
        self.radius = radius

    def draw(self):
        self.renderer.render_circle(self.radius)

# Usage
vector = VectorRenderer()
raster = RasterRenderer()

circle1 = Circle(vector, 5)
circle2 = Circle(raster, 10)

circle1.draw()  # Output: Drawing a circle with radius 5 using vector rendering
circle2.draw()  # Output: Drawing pixels for a circle with radius 10
```

### Example 2: Device & Remote Control
```python
from abc import ABC, abstractmethod

# Implementor
class Device(ABC):
    @abstractmethod
    def turn_on(self):
        pass
    
    @abstractmethod
    def turn_off(self):
        pass

# Concrete Implementors
class TV(Device):
    def turn_on(self):
        print("Turning on the TV")
    
    def turn_off(self):
        print("Turning off the TV")

class Radio(Device):
    def turn_on(self):
        print("Turning on the Radio")
    
    def turn_off(self):
        print("Turning off the Radio")

# Abstraction
class RemoteControl(ABC):
    def __init__(self, device: Device):
        self.device = device
    
    @abstractmethod
    def toggle_power(self):
        pass

# Refined Abstraction
class BasicRemote(RemoteControl):
    def toggle_power(self):
        print("Toggling power...")
        self.device.turn_on()
        self.device.turn_off()

# Usage
if __name__ == "__main__":
    tv = TV()
    radio = Radio()
    
    remote = BasicRemote(tv)
    remote.toggle_power()
    
    remote = BasicRemote(radio)
    remote.toggle_power()
```

## Benefits of Bridge Pattern
✅ Reduces class explosion.
✅ Improves code maintainability and scalability.
✅ Allows independent extension of abstraction and implementation.
✅ Improves flexibility by using composition instead of deep inheritance.

## When to Use the Bridge Pattern?
- When you have multiple orthogonal class hierarchies that need to vary independently.
- When subclassing leads to an explosion of classes.
- When you want to switch implementations at runtime.

## Summary
The **Bridge Pattern** helps create a flexible and scalable design by replacing deep inheritance with composition. It allows abstractions and implementations to vary independently, making the system easier to maintain and extend.

---
### References
- "Design Patterns: Elements of Reusable Object-Oriented Software" by Gamma, Helm, Johnson, and Vlissides (Gang of Four).
- Various online programming resources and tutorials.
- Read this blog for Bridge - https://refactoring.guru/design-patterns/bridge
