# class car:
#     def __init__(self,make,model):
#      self.make=make
#      self.model=model
# car1=car("toyota","canberry")
# car2=car("audi","a1")
# print(car1.make,car1.model)
# print(car2.make,car2.model)

# class bank_Acc:
#     def __init__(self,acc_num,bal):
#         self._acc_num=acc_num
#         self._bal=bal
#     def get_bal(self):
#         return self._bal
# acc1=bank_Acc(12345,1000)
# print(acc1.get_bal())
# print(acc1._acc_num())


#object are real life e ntities,it is a instance of a class
# _init_ method --- specific instance
# self -------------- for 

# class bank:
#     def __init__(self,bank_acc,balance):
#         self._bank_acc=bank_acc
#         self.__balance=balance
        
#     def get_balance(self):
#         return self.__balance        
    
# # encapsulation
# # private-----------  __variable
# # protected---------  _variable    
    
    
# g a proteb1=bank(123456789,20000)
# print(b1.get_balance())  #---accessing a private member
# print(b1._bank_acc)      #---accessincted member



class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Bark"

class Cat(Animal):
    def speak(self):
        return "Meow!"

dog = Dog("None")
cat = Cat("Whiskers")

print(dog.name, dog.speak())
print(cat.name, cat.speak())

