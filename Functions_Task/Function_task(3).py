#---------3️⃣ Named Function — Without Input & With Return---------
# #1.Return the sum of numbers from 1 to 100
# def sum_num():
#     sum=0
#     for i in range(1,101):
#         sum+=i
#     return sum
# print(sum_num())

# #2.Return the count of even numbers from 1 to 100
# def even_num():
#     count=0
#     for i in range(1,101):
#         if i%2==0:
#             count+=1
#     return count
# print(even_num())

# #3.Return the sum of all prime numbers from 1 to 100
# def sum_prime():
#     sum=0
#     for i in range(1,101):
#         count=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             sum+=i
#     return sum
# print(sum_prime())


# #4.Return the largest prime number below 100
# def max_prime():
#     for i in range(100,0,-1):
#         count=0
#         for j in range(1,i+1,1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             return i
        
# print(max_prime())

# #5.Return the number having the maximum number of divisors between 1 and 100
# def max_divisors():
#     count=0
#     new=0
#     for i in range(1,101):
#         c=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 c+=1
#          if c>count:
#                 count=c
#                 new=i
#     return new
# print(max_divisors())


# #6.Return the first perfect number between 1 and 10,000
# def perfect_num():
#     for i in range(1,10001):
#         sum=0
#         for j in range(1,i):
#             if i%j==0:
#                 sum+=j
#         if sum==i:
#             return i
# print(perfect_num())

# #7.Return the first Armstrong number greater than 500
# def armstrong():
#     n=500
#     while n>0:
#         new=n
#         g=n
#         count=0
#         sum=0
#         while new>0:
#             ld=new%10
#             count+=1
#             new=new//10
#         while g>0:
#             last=g%10
#             sum=sum+(last**count)
#             g=g//10
        
#         if sum==n:
#             return n
#         n=n+1

# print(armstrong())



# #8.Return the first number having exactly 3 divisors
# def divisors():
#     n=1
    
#     while True:
#         count=0
#         for i in range(1,n+1):
#             if n%i==0:
#               count+=1 
#         if count==3:
#             return n 
#         n=n+1

# print(divisors())


# #9.Return the first number between 100 and 1000 whose digit sum equals its digit product
# def num():
#     for i in range(100,1001):
#         n=i
#         sum=0
#         product=1
#         while n>0:
#             ld=n%10
#             sum+=ld
#             product*=ld
#             n=n//10
#         if sum==product:
#             return i
# print(num())



#10.Return the sum of all numbers between 1 and 1000 that are both palindrome and prime
def both():
    sum=0
    for i in range(1,1001):
        n=i
        def palindrom():
            new=n
            rev=0
            while new>0:
                ld=new%10
                rev=rev*10+ld
                new=new//10
            if i == rev :
                return rev
        def prime():
            count=0
            for j in range(1,i+1):
                if i%j==0:
                    count+=1
            if count==2:
                return i
        if palindrom() and prime():
            sum+=i 
    return sum

print(both())