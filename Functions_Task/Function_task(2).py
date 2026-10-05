#---------2️⃣ Named Function — With Input & Without Return---------
# #1.Print all even numbers from 1 to n
# def even_num(n):
#     for i in range(1,n+1,1):
#         if i%2==0:
#             print(i)
# even_num(18)

# #2.Print the multiplication table of n
# def multiplication(n):
#     for i in range(1,n+1):
#         for j in range(1,11):
#             print(f"{i} X {j} ={i*j} ")
#         print()
# multiplication(7)

# #3.Print all prime numbers from 1 to n
# def prime(n):
    
#     for i in range(1,n+1,1):
#         count=0
#         for j in range(1,i+1,1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             print(i)
# prime(600)


# #4.Print all factors of n

# def factors(n):
#     print(f"The factors of {n} :")
#     for i in range(1,n+1,1):
#         if n%i==0:
#             print(i)
# factors(717)


# #5.Print the sum of proper divisors of n
# def divisors(n):
#     sum=0
#     for i in range(1,n+1,1):
#         if n%i==0:
#             sum+=i
#     print(f"The sum of divisors of {n} is : {sum}")
# divisors(64)

# #6.Print whether n is a perfect number
# def perfect(n):
#     sum=0
#     for i in range(1,n):
#         if n%i==0:
#             sum+=i
#     if sum==n:
#         print(f"{n} is a perfect Number")
#     else:
#         print("Not a perfect number")
# perfect(6)


# #7.Print whether n is an Armstrong number
# def armstorng(n):
#     new=n
#     g=n
#     count=0
#     sum=0
#     while n>0:
#         ld=n%10
#         count+=1
#         n=n//10
#     while new>0:
#         l=new%10
#         sum+=l**count
#         new=new//10
#     if sum==g:
#         print(f"{g} is armstrong number")
#     else:
#         print(f"{g} is Not a armstrong number")
# armstorng(370)


# #8.Print all Armstrong numbers from 1 to n
# def arm(n):
#     for i in range(1,n+1,1):
#         new=i
#         g=i
#         sum=0
#         count=0
#         while i>0:
#             ld=i%10
#             count+=1
#             i=i//10
#         while g>0:
#             l=g%10
#             sum=sum+(l**count)
#             g=g//10
#         if new==sum:
#             print(new)
# arm(1000)


# #9.Print the first number after n that is a palindrome and prime
# def check(n):
#     while n>0:
#             new=n
#             g=n
#             rev=0
#             count=0
#             while new>0:
#                 ld=new%10
#                 rev=rev*10+ld
#                 new=new//10
#             for i in range(1,n+1):
#                 if n%i==0:
#                     count+=1
#             if count==2 and n==rev:
#                 print(n)
#                 break
#             n=n+1
# check(102)
            
            
            
# # #10.10
# # Print all numbers from 1 to n having exactly 3 divisors

# def three_divisors(n):
    
#     for i in range(1,n+1):
#         count=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 count+=1
#         if count==3:
#             print(i)
# three_divisors(789)
    
    