class student:
    def __init__(self):
        print("Object is created : constructor is Invoked")
    def __del__(self):
        print("Object is going to destroyed : Destructor is Invoked")

s1 = student()
print("We gonna delete object ---- Manually")
del s1
print("Program deleted")