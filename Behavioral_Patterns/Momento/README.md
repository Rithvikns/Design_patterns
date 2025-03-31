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

## Reference

https://refactoring.guru/design-patterns/memento

---
# Python Implementation 
Let's break down the Python implementation of the Memento Design Pattern step by step.

## Memento Class
The Memento class is responsible for storing a snapshot of the Originator's state.

```python
class Memento:
    def __init__(self, state):
        self._state = state

    def get_state(self):
        return self._state
```
It has one private attribute (_state), which stores the object's state.

The get_state() method returns the stored state.

This class is immutable—it doesn't allow modifications after creation.

## Originator Class
The Originator is the main object whose state needs to be saved and restored.

python
Copy
Edit
class Originator:
    def __init__(self):
        self._state = ""  # Default state

    def set_state(self, state):
        print(f"Setting state to: {state}")
        self._state = state  # Updates the internal state

    def save_state(self):
        print(f"Saving state: {self._state}")
        return Memento(self._state)  # Creates a memento with the current state

    def restore_state(self, memento):
        self._state = memento.get_state()  # Restores the saved state
        print(f"Restored state to: {self._state}")
Key Methods:
set_state(state):

Updates the current state.

Prints a message indicating the new state.

save_state():

Saves the current state inside a Memento object.

Returns the Memento so that it can be stored by the Caretaker.

restore_state(memento):

Retrieves the saved state from a Memento and updates the Originator's state.

Prints the restored state.

3. Caretaker Class
The Caretaker manages multiple mementos and provides a way to retrieve them.

python
Copy
Edit
class Caretaker:
    def __init__(self):
        self._mementos = []  # Stores the saved mementos

    def add_memento(self, memento):
        self._mementos.append(memento)  # Saves a memento

    def get_memento(self, index):
        return self._mementos[index]  # Retrieves a saved memento
Key Responsibilities:
Stores Memento objects in _mementos (list).

Provides add_memento() to store a snapshot.

Provides get_memento(index) to retrieve a previously saved state.

4. Client Code (Using the Pattern)
python
Copy
Edit
if __name__ == "__main__":
    originator = Originator()
    caretaker = Caretaker()

    originator.set_state("State 1")
    caretaker.add_memento(originator.save_state())  # Save first state

    originator.set_state("State 2")
    caretaker.add_memento(originator.save_state())  # Save second state

    originator.set_state("State 3")  # Change state without saving

    print("\nUndoing changes...\n")
    originator.restore_state(caretaker.get_memento(0))  # Restore first state
Execution Steps:
Create Originator and Caretaker.

Set "State 1" and save it in Caretaker.

Set "State 2" and save it.

Set "State 3" but do not save it.

Restore "State 1" using the first saved Memento.

Output
perl
Copy
Edit
Setting state to: State 1
Saving state: State 1
Setting state to: State 2
Saving state: State 2
Setting state to: State 3

Undoing changes...

Restored state to: State 1
What Happens?
The originator changes state multiple times.

The caretaker stores snapshots of "State 1" and "State 2".

The program restores "State 1" (undo operation).

🔹 Key Takeaways
✅ Encapsulation Maintained: Memento keeps state private, so no external class modifies it directly.
✅ Undo/Redo Enabled: The caretaker allows rolling back to previous states.
✅ Scalability: More states can be added and retrieved efficiently.

This is useful in real-world applications like text editors (undo feature), game checkpoints, and transactional systems.


