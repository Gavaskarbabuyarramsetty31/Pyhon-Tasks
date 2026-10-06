# class Bank:
#     b_name="SBI"
#     Branch="KPHB colony"
#     def __init__(self,name,age,balence,adress):
#         self.name=name
#         self.age=age
#         self.balence=balence
#         self.adress=adress
        
#     def display(self):
#         print("customer Name : ",self.name)
#         print("customer Age : ",self.age)
#         print("customer Address : ",self.adress)
#         print("customer Balence : ",self.balence)
        
#         print("Bank Name :",Bank.b_name)
#         print("Branch Name :",Bank.Branch)
        
# c1=Bank("Gavaskar","21","Guntur","Rs 7,000")
# c2=Bank("Mike","34","Goa","Rs 57,000")
# c3=Bank("Venky","28","Nellore","Rs 300")
# c4=Bank("Steve","35","Hyderabad","Rs 8,37,000")

# print("---Coustomer 1 Details ------")
# c1.display()
# print("---Coustomer 2 Details ------")
# c2.display()
# print("---Coustomer 3 Details ------")
# c3.display()
# print("---Coustomer 4 Details ------")
# c4.display()


        
        
# class Max:
#     driver="Max verstapan"
#     team="Red Bull"
#     def __init__(self,track,Position,points,lap):
#         self.track=track
#         self.Positon=Position
#         self.points=points
#         self.f_lap=lap
        
#     def display(self):
#         print("Driver Name : ",Max.driver)
#         print("Team Name : ",Max.team)
        
#         print("Track Name : ",self.track)
#         print("Position : ",self.Positon)
#         print("Fastest lap: ",self.f_lap)
#         print("Points    : ",self.points)
        
        
        
# r1 = Max("Bahrain", 1, 25, "1:32.608")
# r2 = Max("Saudi Arabia", 2, 18, "1:30.865")
# r3 = Max("Australia", 1, 25, "1:19.813")
# r4 = Max("Japan", 3, 15, "1:30.983")
# r5 = Max("Monaco", 4, 12, "1:14.165")

# print("---Race 1 Details ------")
# r1.display()
# print("---Race 2 Details ------")
# r2.display()
# print("---Race 3 Details ------")
# r3.display()
# print("---Race 4 Details ------")
# r4.display()
# print("---Race 4 Details ------")
# r5.display()




# class Virat:
#     name="Virat kohli"
#     Batting="Right Hand Batsmen"
#     team="Royal challengers Benguluru"
#     def __init__(self,year,runs,average,sr):
#         self.year=year
#         self.runs=runs
#         self.average=average
#         self.strikerate=sr
#     def display(self):
#         print("Player Name :",Virat.name)
#         print("Batting Style :",Virat.Batting)
#         print("Team Played :",Virat.team)
#         print("Year Played :",self.year)
#         print("Runs Scored :",self.runs)
#         print("Average   :",self.average)
#         print("Strike Rate :",self.strikerate)
        
# s1 = Virat(2020, 466, 34.36, 121.35)
# s2 = Virat(2021, 405, 28.92, 119.46)
# s3 = Virat(2022, 341, 22.73, 115.98)
# s4 = Virat(2023, 639, 53.25, 139.82)
# s5 = Virat(2024, 741, 37.05, 155.50)

# print("----IPL Season 2020-----")
# s1.display()
# print("----IPL Season 2021-----")
# s2.display()
# print("----IPL Season 2022-----")
# s3.display()
# print("----IPL Season 2023-----")
# s3.display()
# print("----IPL Season 2024-----")
# s4.display()
# print("----IPL Season 2025-----")
# s5.display()


# Top 5 Comedy movies in telugu

class  Movie:
    lang="Telugu"
    genre="Comedy"
    def __init__(self,hero,heroine,production,director,movie):
        self.hero=hero
        self.heroine=heroine
        self.production=production
        self.director=director
        self.movie=movie
    def display(self):
        print("Movie Name :",self.movie)
        print("Language :",Movie.lang)
        print("Genre type : ",Movie.genre)
        print("Hero Name : ",self.hero)
        print("Heroine : ",self.heroine)
        print("Director : ",self.director)
        print("production : ",self.production)
        
        
        
m1 = Movie("Allu Arjun", "Ileana D'Cruz", "DVV Danayya", "Trivikram Srinivas", "Julayi")
m2 = Movie("Nani", "Swathi Reddy", "Anil Kumar", "Mohana Krishna Indraganti", "Ashta Chamma")
m3 = Movie("Vishnu Manchu", "Genelia D'Souza", "Sri Venkateswara Creations", "Sreenu Vaitla", "Dhee")
m4 = Movie("Pawan Kalyan", "Shruti Haasan", "Bandla Ganesh", "Harish Shankar", "Gabbar Singh")
m5 = Movie("Nani", "Lavanya Tripathi", "V. Vamsi Krishna Reddy", "Maruthi", "Bhale Bhale Magadivoy")
print("----- Movie 1 Details -----")
m1.display()

print("----- Movie 2 Details -----")
m2.display()

print("----- Movie 3 Details -----")
m3.display()

print("----- Movie 4 Details -----")
m4.display()

print("----- Movie 5 Details -----")
m5.display()


        