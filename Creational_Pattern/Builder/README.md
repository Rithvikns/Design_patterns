"""
A Builder in Python is a design pattern used to construct complex objects step by step.
It provides a clear and readable way to create objects with many configurable attributes.

The Builder pattern is particularly useful when an object has multiple optional parameters or requires a specific construction sequence. It allows developers to create objects in a structured manner while keeping the code clean and maintainable.

Instead of passing numerous parameters to a constructor, the Builder pattern enables setting properties through method chaining. This approach improves code readability and reduces the chances of errors.

### Components of the Builder Pattern:
1. **Product**: The complex object that needs to be created.
2. **Builder**: Defines the steps to build the product.
3. **Concrete Builder**: Implements the Builder interface to construct the product.
4. **Director (Optional)**: Oversees the building process and enforces a construction sequence.

### Diagram Representation:

```
+------------------+
|      Client     |
+------------------+
         |
         v
+------------------+
|     Director    |
+------------------+
         |
         v
+------------------+
|     Builder     |
+------------------+
  |      |      |
  v      v      v
+--------+------+------+
| Concrete Builders  |
+--------+------+------+
         |
         v
+------------------+
|     Product     |
+------------------+
```

The Client interacts with the Director (if present) to build the object. The Director delegates the construction steps to the Builder, which uses a Concrete Builder to assemble the Product.
"""
### Reference
https://refactoring.guru/design-patterns/builder
