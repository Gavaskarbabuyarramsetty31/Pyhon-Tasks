# if(True):
#     print("Condition 1 is true : If block is executed")
# elif(False):
#     print("Condition 1 is False : 1st elif block is executed ")
# elif(False):
#     print("Condition 1&2  is False : 2nd elif block is executed ")
# else:
#     print("All conditions are  False :  else block is executed ")
    
    
    
# if(False):
#     print("Condition 1 is true : If block is executed")
# elif(True):
#     print("Condition 1 is False : 1st elif block is executed ")
# elif(False):
#     print("Condition 1&2  is False : 2nd elif block is executed ")
# else:
#     print("All conditions are  False :  else block is executed ")






#check the given number is positivee or not
# n=int(input("Enter the number :"))
# if(n>0):
#     print(n," is positive number")
# elif(n<0):
#     print(n," is negative number!")
# else:
#     print("Zero!")
    
    


#check given character is alphabet ,digit or symbol:
# ch=input("Enter the character")
# if ((ch>="A" and ch<="Z") or (ch>="a" and ch<="z")):
#     print(ch, " is Alphabet")
# elif(ch>="0" and ch<="9"):
#     print(ch, " ch is digit")
# else:
#     print("stymbol")



n=int(input("Enter the marks :"))
if(n>90):
    print("The Grade: S")
elif(n>=71 and n<=90):
    print("The Grade: A")
elif(n>=51 and n<=70):
    print("The Grade: B")
elif(n>=35 and n<51):
    print("The Grade: C")
else:
    print("The Grade: Fail")