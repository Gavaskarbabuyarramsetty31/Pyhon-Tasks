# class Test:
#     #Special kind of Instance Method
#     def __init__(self):
#         print("I am Constructor")
# t1=Test()
        
# class Test:
#     #Parameterized constructor
#     def __init__(self,name,age):
#         print(f"Hii {name} you are {age} years old !")
# t1=Test("Gavaskar","21")

# class Test:
#     def __init__(self,name):
#         return None
# t1=Test("Gava")
# print(t1)

class Students:
    ins_name="Innomatics"
    def __init__(self,name,age,course):
        self.myname=name
        self.myage=age
        self.mycourse=course
    def display(self):
        print("Name :",self.myname)
        print("age :",self.myage)
        print("course :",self.mycourse)
        print("Institute:",Students.ins_name)
        
s1=Students("gavaskar","21","Python")
s2=Students("Gopi","23","Java")
s3=Students("Govardhan","21","Fullstack")
print("------student 1------")
s1.display()
print("------student 2------")
s2.display()
print("------student 3------")
s3.display()
        
        

        