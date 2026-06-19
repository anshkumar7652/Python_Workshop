from abc import ABC, abstractmethod
class comp(ABC):
    @abstractmethod
    def process(self):
        pass
    def message(self):
        print('Computer is an electronic device')

class laptop(comp):
    def process(self):
        print('Executive laptop progress')

class desktop(comp):
    def process(self):
        print('Executive desktop progress')

com1=laptop()
com2=desktop()
com1.process()
com2.message()
com2.process()