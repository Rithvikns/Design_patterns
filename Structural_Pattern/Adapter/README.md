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
```python
class ModernPrinter:
    def print_text(self, text):
        return f"Modern Printer Output: {text}"
```

## Adapter class to make OldPrinter compatible with ModernPrinter's interface
```python
class PrinterAdapter:
    def __init__(self, old_printer):
        self.old_printer = old_printer
    
    def print_text(self, text):
        # Adapting old_print method to new print_text method
        return self.old_printer.old_print(text)
```
# Usage
```python
old_printer = OldPrinter()
adapted_printer = PrinterAdapter(old_printer)
```
# The new system expects print_text method
```python
print(adapted_printer.print_text("Hello, Adapter Pattern!"))
```

## Use Case Scenario

In this example, we deal with multiple payment gateways (PayPal, Stripe, Razorpay),
each with its own unique interface. Instead of modifying each legacy class,
 we create adapters that translate the old methods into a standard interface.

## Key Components:
1. **Legacy Classes (PayPal, Stripe, Razorpay)** - These classes represent existing systems with different methods to process payments.
2. **Target Interface (PaymentProcessor)** - This is the expected interface in the new system.
3. **Adapter Classes (PayPalAdapter, StripeAdapter, RazorpayAdapter)** - These classes wrap the legacy classes and implement the common interface by delegating the calls appropriately.
4. **Client Code** - Uses the adapters to interact with different payment gateways uniformly.

## Benefits:
- Enables integration of legacy systems without modifying their code.
- Provides a clean and consistent interface for clients.
- Enhances maintainability and flexibility by separating concerns.

## Usage:
- The client instantiates adapter objects for each payment gateway and calls the `pay` method.
- The adapters internally call the appropriate method on the legacy class, ensuring seamless compatibility.
  
## Example Output:
```console
 Processed $100 using PayPal.
 Paid $100 via Stripe.
 Transaction of $100 started with Razorpay.
```
