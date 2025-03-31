# Memento Design Pattern

## Overview
The **Memento Pattern** is a behavioral design pattern that allows an object's state to be captured and restored later without violating encapsulation. This is useful for implementing undo/redo functionality.

## Intent
- Save and restore an object's state without exposing its internal structure.
- Preserve encapsulation boundaries.
- Facilitate undo/redo operations.

## Structure
The Memento Pattern consists of three main components:

1. **Originator**: The object whose state needs to be saved.
2. **Memento**: A snapshot of the Originator's state.
3. **Caretaker**: Manages the memento's lifecycle but does not modify its contents.

## UML Diagram
```
+-------------+      +-------------+      +-------------+
|  Originator |      |   Memento   |      |  Caretaker  |
+-------------+      +-------------+      +-------------+
| state       |      | state       |      | mementoList |
| saveState() |----->| (immutable) |      | addMemento()|
| restore()   |<-----|             |      | getMemento()|
+-------------+      +-------------+      +-------------+
```


## Use Cases
- **Undo/Redo functionality** in applications.
- 
- **Checkpoint systems** in games.
- **Transactional operations** where rollback is needed.

## Pros and Cons
### ✅ Advantages:
- Maintains encapsulation.
- Supports undo/redo mechanisms.
- Simplifies state restoration.

### ❌ Disadvantages:
- Can consume a lot of memory if many states are stored.
- Managing mementos efficiently can be complex.

## Related Patterns
- **Command Pattern** (can use Memento for undo functionality).
- **Prototype Pattern** (alternative approach to saving object state).

## Conclusion
The Memento Pattern is essential for preserving object state in a controlled manner while maintaining encapsulation. It is widely used in applications requiring rollback or undo capabilities.

---
**Feel free to contribute or improve this repository!** 🚀


