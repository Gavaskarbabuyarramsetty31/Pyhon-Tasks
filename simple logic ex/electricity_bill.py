unit=int(input("Enter the no of units :"))
if (unit>=0 and unit<=100):
    print(f"Current Bill Amount= {unit*2}")
elif(unit>=101 and unit<=200):
    print(f"Curren Bill Amount ={unit*4}")
elif(unit>=201 and unit<=300):
    print(f"Curren Bill Amount ={unit*6}")
elif(unit>=301):
    print(f"Curren Bill Amount ={unit*8}")
else:
    print("Enter the Valid Units")
