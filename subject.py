"""Subject class"""


class Subject:
    def __init__(self):
        self.observers = []

    def addObserver(self, observer):
        if observer not in self.observers:
            self.observers.append(observer)

    def removeObserver(self, observer):
        self.observers.remove(observer)

    def notify(self, event, updated_text):
        for observer in self.observers:
            observer.notify(event, updated_text)
