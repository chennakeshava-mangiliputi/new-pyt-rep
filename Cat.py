# class Cat:
#     def make_sound(self):
#         print("Cat is making sound")
# class Dog(Cat):
#     def make_sound(self):
#         print("Dog is making sound")
# for v in(Cat(),Dog()):
#     v.make_sound()
#
#
#
#
#
# #overloading example     polymorphism
# class Demo:
#     def show(self,a=None,b=None,c=None):
#         if a and b and c:
#             print("three args")
#         elif (a and b) or (a and c):
#             print("two args")
#         if a or b or c:
#             print("one args")
#         else:
#             print("no args")
# obj=Demo()
# obj.show(1,2,3)
# obj.show(1,2)
# obj.show(1)





#abstract classes example
# from abc import ABC, abstractmethod
# class PaymentMethod(ABC):
#     @abstractmethod
#     def pay(self,amount):
#         pass
#     @abstractmethod
#     def online(self,amount):
#         pass
# class UPI(PaymentMethod):
#     def pay(self,amount):
#         print(f"{amount} Paid using upi")
#     def online(self,amount):
#         print("amount paid online")
# obj=UPI()
# obj.online(100)
# obj.pay(200)


