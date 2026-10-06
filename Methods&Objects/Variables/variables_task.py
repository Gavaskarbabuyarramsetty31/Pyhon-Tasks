#-------FIRST EXAMPLE--------

# class adhaar:
#     country="India"
#     def assigndata(self,name,number,age):
#         self.name=name
#         self.number=number
#         self.age=age
#     def displaydata(self):
#         print("Name   : ",self.name)
#         print("Number : ",self.number)
#         print("Age    : ",self.age)
#         print("Country: ",adhaar.country)        
        
# p1=adhaar()
# p1.assigndata("Gavaskar","7999 1202 7268","21")
# print("-----Person1----")
# p1.displaydata()

# p2=adhaar()
# p2.assigndata("Pawan kalyan","3921 2032 7892","45")
# print("-----Person2----")
# p2.displaydata()

# p3=adhaar()
# p3.assigndata("Thala","7777 0707 7070","77")
# print("-----Person2----")
# p3.displaydata()
        
        
        
# ##-------Second EXAMPLE--------
# #top 4 batsment in csk history
# class Csk:
#     team="Chennai Super Kings"
#     def assigndata(self,Place,Name,Runs):
#         self.place=Place
#         self.name=Name
#         self.runs=Runs
#     def displaydata(self):
#         print("Rank : ",self.place)
#         print("Name :",self.name)
#         print("Runs :",self.runs)
#         print("Team :",Csk.team)
        
# p1=Csk()
# p1.assigndata("1","M.S DHONI","4,865")
# print("-----Player 1------")
# p1.displaydata()

# p1=Csk()
# p1.assigndata("2","Suresh Raina","4,687")
# print("-----Player 2------")
# p1.displaydata()

# p1=Csk()
# p1.assigndata("3","Ruturaj Gaikwad","2,753")
# print("-----Player 3------")
# p1.displaydata()
        
#Third Example
#pawan kalyan well-known  five movies 
class Pawan_kalyan:
    hero="Pawan Kalyan"
    def assigndata(self,m_name,heroine,director,status):
        self.m_name=m_name
        self.heroine=heroine
        self.director=director
        self.status=status      
    def displaydata(self):
        print("movie name:" ,self.m_name)
        print("   Hero   :",Pawan_kalyan.hero)
        print(" Heroine  :" ,self.heroine)
        print(" Director :" ,self.director)
        print(" Status   :" ,self.status)
        

m1=Pawan_kalyan()
print("------First Movie------")
m1.assigndata("OG","Priyanka Mohan","Sujeeth","Blockbuster")
m1.displaydata()

m2 = Pawan_kalyan()
print("\n------Second Movie------")
m2.assigndata("Gabbar Singh", "Shruti Haasan", "Harish Shankar", "Blockbuster")
m2.displaydata()

m3 = Pawan_kalyan()
print("\n------Third Movie------")
m3.assigndata("Jalsa", "Ileana D'Cruz", "Trivikram Srinivas", "Blockbuster")
m3.displaydata()

m4 = Pawan_kalyan()
print("\n------Fourth Movie------")
m4.assigndata("Attarintiki Daredi", "Samantha Ruth Prabhu", "Trivikram Srinivas", "Blockbuster")
m4.displaydata()

m5 = Pawan_kalyan()
print("\n------Fifth Movie------")
m5.assigndata("Panjaa", "Sarah Jane Dias", "Vishnuvardhan", "Average")
m5.displaydata()