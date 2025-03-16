# Proxy Pattern in Python

This repository demonstrates the **Proxy Design Pattern** in Python. The proxy pattern is used to **control access** to an object by placing another object (proxy) as an intermediary.

## **Overview**
A proxy is a placeholder or intermediary for another object. It can be used for:
- **Access control** (restricting unauthorized access)
- **Logging & Monitoring** (tracking requests)
- **Lazy Initialization** (delaying expensive operations until necessary)
- **Caching** (storing results for efficiency)

## **Code Explanation**

### **1. Define an Interface (Abstract Class)**
```python
from abc import ABC, abstractmethod

class Subject(ABC):
    @abstractmethod
    def request(self):
        pass
```
- `Subject` is an abstract base class.
- It defines `request()`, which must be implemented by subclasses.

### **2. Implement the Real Object (RealSubject)**
```python
class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request...")
```
- `RealSubject` is the actual object that performs the operation.

### **3. Implement the Proxy Class**
```python
class Proxy(Subject):
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        if self.check_access():
            self._real_subject.request()
            self.log_access()
        else:
            print("Proxy: Access denied.")
    
    def check_access(self):
        print("Proxy: Checking access...")
        return True  # Simulating access control
    
    def log_access(self):
        print("Proxy: Logging access...")
```
- The **Proxy** class controls access to `RealSubject`.
- It performs **access checks** before forwarding requests.
- It also **logs access** after forwarding requests.

### **4. Client Code**
```python
if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    
    print("Client: Using the proxy to request service...")
    proxy.request()
```
- The client interacts with the `Proxy` instead of `RealSubject`.
- The `Proxy` ensures security and logging before delegating the request.

## **Use Cases in GitHub Projects**
- **Security**: Restrict access to certain functions.
- **Logging**: Track usage and API calls.
- **Lazy Loading**: Load resources only when needed.
- **Caching**: Store results to improve efficiency.

## **Running the Code**
```bash
python proxy.py
```

## **Conclusion**
This implementation of the **Proxy Pattern** helps in controlling access and enhancing functionality without modifying the real object.

## Reference
For more information on proxy you can refer this website https://refactoring.guru/design-patterns/proxy
