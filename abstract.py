from abc import ABCMeta, abstractmethod

class lang_program(metaclass=ABCMeta):
    @abstractmethod
    def Supports_OOP(self):
    #  return 'Yes'
        pass
        
    def say_hello(self):
        return "hello"
class Python(lang_program):
    def Supports_OOP(self):
        return 'Yes'
    
class C(lang_program):
    def Supports_OOP(self):
        return 'No'
    
    
My_lang=Python()
print(My_lang.Supports_OOP())


    

