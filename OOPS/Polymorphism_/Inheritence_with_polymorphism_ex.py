# 1.1.Single Inheritance + Polymorphism (Method Overriding)
# class Tackel:
#     def __init__(self,name,tackels):
#         self.name=name
#         self.tackels=tackels
#     def displaytackel(self):
#         print("-----While Normal Tackel----")
#         print("Player name = ",self.name)
#         print("Player Tackel = ",self.tackels)
#         print("Player points = ",self.tackels)

# class SuperTackels(Tackel):
#     def __init__(self,name,tackels):
#         super().__init__(name,tackels)
#     def displaytackel(self):
#             print("------While super Tackel is on ------")
#             print("Player name = ",self.name)
#             print("Player Tackel = ",self.tackels)
#             print("Player points = ",self.tackels * 2)

# t=Tackel("Surender nada",20)
# st=SuperTackels("Surender nada",20)

# t.displaytackel()
# st.displaytackel()


# #1.2.Single Inheritance + Polymorphism (Method Overriding)

# class Odi:
#     def powerplay(self):
#         print("1-10 overs poweplay")
# class T20(Odi):
#     def powerplay(self):
#         print("1-6 overs Powerplay")

# o=Odi()
# t=T20()

# o.powerplay()
# t.powerplay()


# # 2.1 multilevel inheritance + polymorphism problems

# class Ticket:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

#     def ticketdetails(self):
#         print("---In Theater ------")
#         print("Movie name : ", self.name)
#         print("Type =  Directly on theater counter")
#         print("Ticket Price : ", self.price)


# class Onlineticket(Ticket):
#     def __init__(self, name, price):
#         super().__init__(name, price)
#         self.online_charge = (self.price*1.5/10)

#     def ticketdetails(self):
#         print("-----Online Booking ------")
#         print("Movie name : ", self.name)
#         print("Type =  In Online Booking")
#         print("Ticket Price : ", self.price+self.online_charge)


# class Imax(Onlineticket):
#     def __init__(self, name, price):
#         super().__init__(name, price)
#         self.imax = (self.price*3/10)

#     def ticketdetails(self):
#         print("------In Imax Booking -------")
#         print("Ticket type : ", self.name)
#         print("Type =  At Imax ")
#         print("Ticket Price : ", self.price+self.online_charge+self.imax)

# t=Ticket("OG",250)
# o=Onlineticket("OG",250)
# i=Imax("OG",250)


# t.ticketdetails()
# o.ticketdetails()
# i.ticketdetails()


# # 2.2 multilevel inheritance + polymorphism problems

# class Basicsalary:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_salary(self):
#         print("Name = ", self.name)
#         print("Basic Salary = ", self.salary)


# class Pfsalary(Basicsalary):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
#         self.pf = self.salary*12/100

#     def display_salary(self):
#         print("----Salary after Pf deduction ------")
#         print("Name = ", self.name)
#         print(" Salary = ", self.salary-self.pf)


# class Loansalary(Pfsalary):
#     def __init__(self, name, salary):
#         super().__init__(name, salary)
#         self.loan=35000

#     def display_salary(self):
#         print("----Salary after Pf & loan deduction ------")
#         print("Name = ", self.name)
#         print("Remaining Salary = ", (self.salary-self.pf)-self.loan)

# b=Basicsalary("Gavaskar",90000)
# p=Pfsalary("Gavaskar",90000)
# l=Loansalary("Gavaskar",90000)


# b.display_salary()
# p.display_salary()
# l.display_salary()

# # 3.1 Heirarchieal inheritance + polymorphism problems

# class Loan:
#     def __init__(self, name, loan, time):
#         self.name = name
#         self.loan = loan
#         self.time = time

#     def displaydetails(self):
#         print("Customer Name = ", self.name)
#         print("Loan Amount = ", self.loan)
#         print(f"Tenture/Time =  {self.time} years")


# class CarLoan(Loan):
#     def __init__(self, name, loan, time):
#         super().__init__(name, loan, time)
#         self.interst = self.loan*8.5/100
#         self.car_price = 3400000
#         self.down_payent = 600000

#     def displaydetails(self):
#         print("------car Loan details ---------")
#         super().displaydetails()
#         print("Intrest rate = 8.5 %")
#         print(f"Intrest_rate = {self.interst} per year")
#         print("Car price = ", self.car_price)
#         print("Down Payment = ", self.down_payent)


# class Homeloan(Loan):
#     def __init__(self, name, loan, time):
#         super().__init__(name, loan, time)
#         self.homeintrest = self.loan*9/100
#         self.propery_value = 9845000

#     def displaydetails(self):
#         print("------Home Loan details ---------")
#         super().displaydetails()
#         print("Intrest rate = 9.0 %")
#         print(f"Intrest_rate = {self.homeintrest} per year")
#         print("Property Value price = ", self.propery_value)


# l=Loan("Gavaskar",2000000,9)
# c=CarLoan("Gavaskar",2000000,9)
# h=Homeloan("Gavaskar",2000000,9)

# l.displaydetails()
# c.displaydetails()
# h.displaydetails()


# class Employees:
#     def __init__(self, name, id, salary):
#         self.name = name
#         self.id = id
#         self.salary = salary

#     def calculatesalary(self):
#         print("-------Employee details------")
#         print("Name = ", self.name)
#         print("Id = ", self.id)
#         print("Basic Salary = ", self.salary)


# class PermanentEmployee(Employees):
#     def __init__(self, name, id, salary):
#         super().__init__(name, id, salary)
#         self.pf = (self.salary*12/100)
#         self.da = (self.salary*20/100)
#         self.hra = (self.salary*40/100)
#         self.grosssalary = (self.salary+self.da+self.hra)
#         self.netsalary = (self.grosssalary-self.pf)

#     def calculatesalary(self):
#         print("-------Salary for Permenant Employee-----")
#         super().calculatesalary()
#         print("HRA = ", self.hra)
#         print("DA =", self.da)
#         print("PF = ", self.pf)
#         print("Gross_salary =", self.grosssalary)
#         print("Net Salary =", self.netsalary)


# class Intern(Employees):
#     def __init__(self, name, id, salary):
#         super().__init__(name, id, salary)
#         self.bonus = (self.salary*7/100)
#         self.stipend = (self.salary+self.bonus)

#     def calculatesalary(self):
#         print("-------Salary for Intern -------")
#         super().calculatesalary()
#         print("Bonus = ", self.bonus)
#         print("Inhand Stipend = ", self.stipend)


# e = Employees("Gavaskar", 7731, 30000)
# p = PermanentEmployee("Gavaskar", 7731, 30000)
# i = Intern("Gavaskar", 7731, 30000)

# e.calculatesalary()
# p.calculatesalary()
# i.calculatesalary()



