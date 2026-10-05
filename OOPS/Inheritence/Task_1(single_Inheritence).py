# #1.Single Inheritance without constructor

# class Parent():
#     def Property(self):
#         print("Parents property")
#     def debts(self):
#         print("Parents Debts")
#     def genetics(self):
#         print("Parent Genetics")
# class Child(Parent):
#     def new(self):
#         print("new Properties")
        
# c=Child()
# c.Property()
# c.debts()
# c.genetics()
# c.new()



# #2.Single Inheritance with constructor
# class car:
#     def __init__(self,colour,model,price):
#         self.colour=colour
#         self.model=model
#         self.price=price
#     def displaydata(self):
#         print("Car Model= ",self.model)
#         print("Car Price= ",self.price)
#         print("Car Colour= ",self.colour)
# class Ford(car):
#     pass

# f=Ford("Black","2019","4050000/-")
# f.displaydata()



# 3.Single Inheritance with constructor + super()

# class team():
#     def __init__(self,budget,slots,i_slots,o_slots,w_slot,rtm):
#         self.budget=budget
#         self.total_slots=slots
#         self.indian_slots=i_slots
#         self.overseas_slots=o_slots
#         self.wk_slots=w_slot
#         self.rtm=rtm
#     def displayteam(self):
#         print("Budget = ",self.budget)
#         print("Total Slots = ",self.total_slots)
#         print("Indain Slots = ",self.indian_slots)
#         print("Overseas Slots = ",self.overseas_slots)
#         print("Wk Slots = ",self.wk_slots)
#         print("RTM = ",self.rtm)
        
        
# class Csk(team):
#     def __init__(self,budget,slots,i_slots,o_slots,w_slot,rtm,name,cups):
#         super().__init__(budget,slots,i_slots,o_slots,w_slot,rtm)
#         self.name=name
#         self.cups=cups
#     def displaycsk(self):
#         print("Team Name :",self.name)
#         super().displayteam()
#         print("Championships = ",self.cups)
        
# c=Csk("43.4cr", "9", "5", "4", "0", 0, "CSK", 5)
# c.displaycsk()

        
        
# #4.Single Inheritance with constructor + super() using a different real-world example

# class Batsmen():
#     def __init__(self,style,runs,sixes,fours,sr,avg,name):
#         self.batting_style=style
#         self.runs=runs
#         self.sixes=sixes
#         self.fours=fours
#         self.sr=sr
#         self.avg=avg
#         self.name=name
#     def displaybatsmen(self):
#         print("----Batting Stats -------")
#         print("Player Name = ",self.name)
#         print("Batting Style = ",self.batting_style)
#         print("Runs Scored = ",self.runs)
#         print("Sixes scored = ",self.sixes)
#         print("Fours scored = ",self.fours)
#         print("Strike Rate =",self.sr)
#         print("Average = ",self.avg)

# class Allrounder(Batsmen):
#     def __init__(self,style,runs,sixes,fours,sr,avg,wickets,b_avg,economy,name):
#         super().__init__(style,runs,sixes,fours,sr,avg,name)
        
#         self.wickets=wickets
#         self.economy=economy
#         self.bowling_avearge=b_avg
#     def displayallrounderdata(self):
#         super().displaybatsmen()
#         print("------Bowling stats -------")
#         print("Wickets = ",self.wickets)
#         print("Bowling avg = ",self.bowling_avearge)
#         print("Economy avg",self.economy)

# a=Allrounder("Left handed", 295, 12, 24, 135.78, 29.50, 8, 36.25, 8.05, "Ravindra Jadeja")
# a.displayallrounderdata()
    