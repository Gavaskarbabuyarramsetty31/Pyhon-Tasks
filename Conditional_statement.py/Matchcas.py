# ch=7
# match ch:
#     case 1:
#         print("Case1 is Executed")
#     case 2:
#             print("Case2 is Executed")
#     case 3:
#             print("Case3 is Executed")
#     case 4:
#             print("Case4 is Executed")
#     case _:
#             print("Default case is Executed")



#1.traffic signals
# colour=input("Enter the Colour :")
# match(colour):
#     case "red":
#         print("Stop the Vehicle")
#     case "orange":
#         print("Ready to Go!")
#     case "green" :
#         print("Go!!")
#     case _:
#         print("Wrong color")




#2.shapes
# sides=int(input("enter the sides :"))
# match sides:
#     case 1:
#         print("line")
#     case 2:
#         print("It is not shape")
#     case 3:
#         print("Triangle")
#     case 4:
#         print("Rectangle")
#     case 5:
#         print("pentagon")
#     case 6:
#         print("Hexagon")
#     case _:
#         print("Polygon")




#.date and day
# n=int(input("Enter the no of the day :"))
# match n:
#     case 1:
#         print("Sunday")
#     case 2:
#         print("Monday")
#     case 3:
#         print("Tuesday")
#     case 4:
#         print("Wednesday")
#     case 5:
#         print("Thursday")
#     case 6:
#         print("Friday")
#     case 7:
#         print("Saturday")
#     case _:
#         print("Enter the valid number")





n1=int(input("Enter the Number1 :"))
n2=int(input("Enter the Number2 :"))
print('''Select an option from the given choices:
      1.Additon
      2.Substraction
      3.Divison
      4.Mutiplicaton
      5.Remainder
      ''')
option=int(input("Your Option :"))
match option:
    case 1:
        print("sum =",(n1+n2))
    case 2:
        print("sub =",(n1-n2))
    case 3:
        print("Div =",(n1/n2))
    case 4:
        print("Mul =",(n1*n2))
    case 5:
        print("Remainder =",(n1%n2))
    case _:
        print("Invalid operator")    
        



