from abc import ABC, abstractmethod

# Step 1: Define an interface
class Subject(ABC):
    @abstractmethod
    def request(self):
        pass

# Step 2: Create a RealSubject class (the actual object)
class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request...")

# Step 3: Create a Proxy class that controls access to RealSubject
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

# Step 4: Client code
if __name__ == "__main__":
    real_subject = RealSubject()
    proxy = Proxy(real_subject)
    
    print("Client: Using the proxy to request service...")
    proxy.request()
