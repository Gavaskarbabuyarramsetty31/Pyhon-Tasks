# #1.Multiple Inheritance without constructor
# class car:
#     def Structure(self):
#         print("It has four tyres,one stearing,engine")
# class Ford(car):
#     def  brand(self):
#         print("Ford badge,SUV body,LED lighting,Ford infotainment,Ford safety technology")
# class Ford_Bronco(Ford):
#     def details(self):
#         print("2.3L EcoBoost I-4, 300 HP, 325 lb-ft torque, 4×4, 7-speed manual/10-speed automatic, 33.5-inch max water-fording, 3,500-lb max towing.")

# f=Ford_Bronco()
# f.Structure()
# f.brand()
# f.details()


# # 2.Multiple Inheritance with constructor

# class Employee:
#     def __init__(self, time, salary):
#         self.time_hours = time
#         self.salary = salary

#     def displayedetails(self):
#         print("Time Hours = ", self.time_hours)
#         print("salary = ", self.salary)


# class Manager(Employee):
#     def __init__(self, time, salary, team_size):
#         self.time_hours = time
#         self.salary = salary
#         self.team_size = team_size

#     def managerdetails(self):
#         self.displayedetails()
#         print("Time Hours = ", self.time_hours)
#         print("salary = ", self.salary)
#         print("Team Size =", self.team_size)


# class SeniorManager(Manager):

#     def __init__(self,  time, salary, team_size, department):
#         self.time_hours = time
#         self.salary = salary
#         self.team_size = team_size
#         self.department = department

#     def seniormanagerdetails(self):
#         print("Time Hours = ", self.time_hours)
#         print("salary = ", self.salary)
#         print("Team Size =", self.team_size)
#         print("Department =", self.department)
        
# s = SeniorManager(8, 80000, 10, "IT")
# s.displayedetails()
# s.managerdetails()
# s.seniormanagerdetails()




# # 2.Multiple Inheritance with constructor

# class Employee:
#     def __init__(self, time, salary):
#         self.time_hours = time
#         self.salary = salary

#     def displayedetails(self):
#         print("Time Hours = ", self.time_hours)
#         print("salary = ", self.salary)


# class Manager(Employee):
#     def __init__(self, time, salary, team_size):
#         super().__init__(time,salary)
#         self.team_size = team_size

#     def managerdetails(self):
#         super().displayedetails()
#         print("Team Size =",self.team_size)


# class SeniorManager(Manager):

#     def __init__(self,  time, salary, team_size, department):
#         super().__init__( time, salary, team_size)
#         self.department = department

#     def seniormanagerdetails(self):
#         super().managerdetails()
#         print("Department =", self.department)
        
# s = SeniorManager(8, 80000, 10, "IT")
# s.displayedetails()
# s.managerdetails()
# s.seniormanagerdetails()
# m=Manager(7,739383,9)
# m.managerdetails()
# m.displayedetails()
