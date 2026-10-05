# class Parent:
#     def m1(self):
#         print("M1 from Parent")
# class child1(Parent):
#     def m2(self):
#         print("M2 from Child 1")
# class Child2(Parent):
#     def m3(self):
#         print("M3 from Child 2")

# p=Parent()
# p.m1()      #Its own method -->Right
# p.m2()      #child method -->wrong
# p.m3()      #child method -->wrong

# c1=child1()
# c1.m1()         #parent method --->Right
# c1.m2()        #Its own method -->Right
# # c1.m3()        #Sibling Method ---->Wrong



# c2=Child2()
# c2.m1()         #parent method --->Right
# # c2.m2()        #Sibling Method ---->Wrong
# c2.m3()        #Its own method -->Right



# class Employee:
#     def det(self):
#         print("I am Employee")
# class Manager(Employee):
#     def mywork(self):
#         print("I work as manager")
# class Developer(Employee):
#     def mydesig(self):
#         print("I work as developer")
        
# m=Manager()
# m.det()
# m.mywork()



# class Bowler:
#     def __init__(self,name,economy,wickets,matches,five):
#         self.name=name
#         self.economy=economy
#         self.wickets=wickets
#         self.matches=matches
#         self.five=five
#     def displaybowler(self):
#         print("Player Name = ",self.name)
#         print("Matches = ",self.matches)
#         print("Economy = ",self.economy)
#         print("Wickets = ",self.wickets)
#         print("5W haull = ",self.five)
        
# class Spinner(Bowler):
#     def __init__(self,name,economy,wickets,matches,five,googly,leg,flipper,quickone):
#         super().__init__(name,economy,wickets,matches,five)
#         self.flipper=flipper
#         self.legbreak=leg
#         self.googly=googly
#         self.quickone=quickone
#     def displayspinner(self):
#         print("-----Spinner-------")
#         super().displaybowler()
#         print("Googly = ",self.googly)
#         print("Leg Break = ",self.legbreak)
#         print("FLipper =",self.flipper)
#         print("Quickones =",self.quickone)
        

# class Fastbowler(Bowler):
#     def __init__(self,name,economy,wickets,matches,five,yorkers,bouncers,fulllength,slowerone):
#         super().__init__(name,economy,wickets,matches,five)
#         self.yorker=yorkers
#         self.bouncers=bouncers
#         self.fulllength=fulllength
#         self.slowerone=slowerone
#     def displyfastbowler(self):
#         print("-----Fast Bowler ---------")
#         super().displaybowler()
#         print("Yorkers = ",self.yorker)
#         print("Bouncers = ",self.bouncers)
#         print("Full lengths =",self.fulllength)
#         print("Slowerone = ",self.slowerone)


# shane= Spinner("Shane Warne", 3.35, 708, 145, 37, 120, 350, 100, 80)
# shane.displayspinner()
# dale=Fastbowler("Dale Steyn", 3.24, 699, 93, 25, 180, 120, 250, 90)
# dale.displyfastbowler()


        
        