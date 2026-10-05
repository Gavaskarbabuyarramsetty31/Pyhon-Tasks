#general example
# i=1
# while(i<=7):
#     print(i)
#     i=i+1



# # print the sequence 0,5,10,15,20
# i=0
# while(i<=20):
#     print(i)
#     i=i+5




# #print the sequence of 10,9,8,7,6,5    
# i=10
# while(i>=5):
#     print(i)
#     i=i-1




# #display the sequence odf9,6,3,0

# i=9
# while(i>=0):
#     print(i)
#     i=i-3

#2,6,10,14
# i=2
# while i<15:
#     print(i)
#     i=i+4


#print last digit of a number

# n=456
# while n!=0:
#     ld=n%10
#     print(ld)
#     n=n//10


# n=456
# while n!=0:
#     n//10
#     print(n)

# #count the digits in a given number n=37372
# n=37372
# count=0
# while n!=0:
#     # ld=n%10
#     count+=1
#     n=n//10
# print(f"count of digits in a number :{count}")



# #
# n=21829
# new=n
# sum=0
# while n!=0:
#     ld=n%10
#     sum=sum+ld
#     n=n//10
# print(f"The sum of digits in the {new} : {sum}")




# #reverese a number
# n=123828289014
# new=n
# rev=0
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# print(f"the reverse of  {new} is : {rev}")
    
    
    
# #check a palindrom number(if a number and reverse number are equal ,they are palindrom)
# n=123321
# new=n
# rev=0
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# if new==rev:
#     print("The number is palindrom ")
# else:
#     print("! Not palindrom")


# #erite the code to display odd numbers in a number;
# n=1234
# while n>0:
#     ld=n%10
#     if ld%2 !=0:
#         print(ld)
#     n=n//10

# n=456789
# count=0
# while n>0:
#     ld=n%10
#     if ld%2==0:
#         count+=1
#     n=n//10
# print(f"count of even numbers : {count}")



# #find the largest digit in a number :
# n=45667
# large=0
# while n>0:
#     ld=n%10
#     if ld>large:
#         large=ld
#     n=n//10
# print(f"Largest number in the number is : {large}")



# #find the smallest digit in a number :
# n=45667
# small=9
# while n>0:
#     ld=n%10
#     if ld<small:
#         small=ld
#     n=n//10
# print(f"Largest number in the number is : {small}")



