# Adapter Structural Design Pattern in Python

- The Adapter pattern allows objects with incompatible interfaces to work together.
- It acts as a bridge between two different interfaces by wrapping an existing class with a new interface.

# Example:
 Suppose we have a legacy class with an old interface that we want to use in a modern system with a different expected interface.
 Legacy class with an old interface
 ```python
class OldPrinter:
    def old_print(self, text):
        return f"Old Printer Output: {text}"
```

## New system expects a different interface
class ModernPrinter:
    def print_text(self, text):
        return f"Modern Printer Output: {text}"

## Adapter class to make OldPrinter compatible with ModernPrinter's interface
class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer
    
    def print_text(self, text):
        # Adapting old_print method to new print_text method
        return self.old_printer.old_print(text)

# Usage
old_printer = OldPrinter()
adapted_printer = PrinterAdapter(old_printer)

# The new system expects print_text method
print(adapted_printer.print_text("Hello, Adapter Pattern!"))
