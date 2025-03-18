from abc import ABC, abstractmethod

# Observer Interface
class Observer(ABC):
    @abstractmethod
    def update(self, message: str):
        pass

# Concrete Observer
class ConcreteObserver(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, message: str):
        print(f"{self.name} received message: {message}")

# Subject (Observable)
class Subject:
    def __init__(self):
        self._observers = []

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def detach(self, observer: Observer):
        self._observers.remove(observer)

    def notify(self, message: str):
        for observer in self._observers:
            observer.update(message)

# Example Usage
if __name__ == "__main__":
    subject = Subject()
    observer1 = ConcreteObserver("Observer 1")
    observer2 = ConcreteObserver("Observer 2")
    
    subject.attach(observer1)
    subject.attach(observer2)
    
    subject.notify("Hello Observers!")
    
    subject.detach(observer1)
    
    subject.notify("Second Message!")
