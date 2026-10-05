#----------1️⃣ Named Function — Without Input & Without Return--------------
# #1.Print even numbers from 1 to 50
# def even_num():
#     for i in range(1,51,1):
#         if i%2==0:
#             print(i)
            
# even_num()

# #2.Print multiplication tables from 1 to 10
# def tables():
#     for i in range(1,11,1):
#         for j in range(1,11,1):
#             print(f"{i} X {j} = {i*j}")
#         print()
# tables()

# #3.Print all prime numbers from 1 to 100
# def prime_num():
#     print("prime numbers :")
#     for i in range(1,101,1):
#         count=0
#         for j in range(1,i+1,1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             print(f"{i}" ,end=",")
# prime_num()

# #4.Print the sum of all prime numbers from 1 to 100
# def sum_prime():
#     sum=0
#     for i in range(1,101,1):
#         count=0
#         for j in range(1,i+1,1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             sum+=i
#     print(f"The sum of Prime numbers = {sum}")
# sum_prime()

# #5.Print all Armstrong numbers from 1 to 1000
# def armstron_num():
#     for i in range(1,1001):
#         n=i
#         new=i
#         sum=0
#         count=0
#         while n>0:
#             ld=n%10
#             count+=1
#             n=n//10
#         while new>0:
#             last=new%10
#             sum=sum+last**count
#             new=new//10
#         if sum==i:
#             print(f"{i} is Armstorng Number ") 
            
# armstron_num()   


# #6.Print all perfect numbers from 1 to 10,000
# def perfect_num():
#     for i in range(1,10001):
#         sum=0
#         for j in range(1,i):
#             if i%j==0:
#                 sum+=j
#         if i==sum:
#             print(f"{i} is a Perfect Number !")
# perfect_num()               
        
            
# #7.Print the first 10 palindrome numbers
# def palindrom():
#     i=1
#     count=0
#     while i>0:
#         rev=0
#         n=i
#         while n>0:
#             ld=n%10
#             rev=rev*10+ld
#             n=n//10
#         if rev==i:
#             print(i)
#             count+=1
#         if count==10:
#             break
#         i=i+1
# palindrom()            
        
            
            
# #8.Find the first number between 1 and 500 having exactly 3 divisors
# def divisor():
#     for i in range(1,501):
#         count=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 count+=1
#         if count==3:
#             print(f"{i} have 3 divisor  ")
#             break
# divisor()

#9.Find the first 5 numbers having exactly 4 divisors
# def four():
#     i=1
#     c=0
#     while i>0:
#         count=0
#         for j in range(1,i+1,1):
#             if i%j==0:
#                 count+=1
#         if count==4:
#             print(f"{i} have four divisors ")
#             c+=1
#         i=i+1
#         if c==5:
#             break
# four()

# #10.Print all numbers between 1 and 1000 whose sum of digits is equal to the product of their digits
# def sum():
#     for i in range(1,1001):
#         n=i
#         sum=0
#         product=1
#         while n>0:
#             ld=n%10
#             sum=sum+ld
#             product*=ld
#             n=n//10
#         if sum==product:
#             print(i)
            
# sum()
            