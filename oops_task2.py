#polymorphism
#method overloading
class operation():
    def mul(self,a=None,b=None,c=None):
        print(a,b,c)
res=operation()
res.mul(10,20,30)
res.mul(10,20)
res.mul(10,30)

#method overriding
class operation():
    def mul(self,a):
        print(a)
class operation1(operation):
    def mul1(self,a):
        print(a)
        super().mul(20)
obj=operation1()
obj.mul1(100)


#encapsulation
#public
class operation():
    def __init__(self,a):
        self.a=a
        print(a)
class operation1(operation):
    def mul1(self,a):
        print(a)

obj=operation1(100)
obj.mul1(20)


#private
class operation():
    def __init__(self,a):
        self.__a=a
        print(self.__a)
class operation1(operation):
    def mul1(self,):
        print("hey")
obj=operation1(100)
obj.mul1

#protected
class operation():
    def __init__(self,a):
        self._a=a
        print(self._a)
class operation1(operation):
    def mul1(self,):
        print("hi")
obj=operation1(200)
obj.mul1()

 #abstraction
from abc import ABC,abstractmethod
class parent():
    @abstractmethod
    def show(self):
        pass
    @abstractmethod
    def show2(self):
        pass
class child(parent):
    def show(self):
        print("hi")
    def show2(self):
        print("hlo")
obj=child()
obj.show()
obj.show2()



