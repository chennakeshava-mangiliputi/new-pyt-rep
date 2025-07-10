class Employee:
    def work(self):
        print("Work")
class Manager(Employee):
    def manage(self):
        print("Managing is my task")
obj=Manager()
obj.work()
obj.manage()





#inheritance example:
class Vehicle:
    def navigate(self):
        pass
class Car(Vehicle):
    def navigate(self):
        print("Car is working")
class Truck(Vehicle):
    def navigate(self):
        print("Truck is working")
for v in [Car(),Truck()]:
    v.navigate()