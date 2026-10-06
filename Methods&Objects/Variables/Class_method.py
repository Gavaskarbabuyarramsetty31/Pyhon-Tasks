# class Test():
#     @classmethod
#     def m1(cls):
#         print("I am Class ")
        
# Test().m1()


# class Student:
#     @classmethod
#     def m1(cls):
#         print("Class Method")
    
#     def m2(self):
#         print("Instance method")
        
# Student.m1()
# s1=Student()
# s1.m2()


class Student:
    institute="Innomatics"
    
    def m1(self):
        self.name="Gavaskar"
        print("Static Variable  = ",self.institute)
        print("Instance Variable  = ",self.name)
    @classmethod
    def m2(cls):
        print("Static Variable  = ",cls.institute)
        print("Static Variable  = ",cls.name)
s1=Student()
s1.m2()
        
        
    
        
        
