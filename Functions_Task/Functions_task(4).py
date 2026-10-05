# #1.Return whether n is even or odd
# def check(n):
#     if n%2==0:
#         return "Even"
#     else:
#         return "odd"
# print(check(19))

# #2.Return the sum of digits of n
# def sum(n):
#     sum=0
#     for i in range(1,n+1,1):
#         sum+=i
#     return sum
# print(sum(81))


# #3.Return the reverse of n
# def reverse(n):
#     new=n
#     rev=0
#     while n>0:
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     return rev
# print(reverse(37929))

# #4.Return whether n is a palindrome
# def check(n):
#     new=n
#     rev=0
#     while n>0:
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     if rev==new:
#         return f"{new} is a Palindrom"
#     else:
#         return f"{new} is  not a Palindrom"
# print(check(112))


# #5.Return whether n is prime

# def check(n):
#     new=n
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     if count==2:
#         return f"{n} is a Prime Number"
#     else:
#         return f"{n} is NOT a prime number"
# print(check(77))

# #6.Return whether n is an Armstrong number
# def check_armstrong(n):
#     new=n
#     count=0
#     sum=0
#     g=n
#     while n>0:
#         ld=n%10
#         count+=1
#         n=n//10
#     while g>0:
#         last=g%10
#         sum+=(last**count)
#         g=g//10
#     if sum==new:
#         return f"{new} is a armstrong number"
#     else:
#         return f"{new} is not a Armstrong number"
# print(check_armstrong(157))
    
    
    
# #7.Return the number of factors of n
# def check_factors(n):
#     count=0
#     for i in range(1,n+1):
#         if n%i==0:
#             count+=1
#     return f"{n} have {count} of factors"
# print(check_factors(60))

# #8.Return the largest proper divisor of n
# def max_divisor(n):
#     max=0
#     for i in range(1,n,1):
#         if n%i==0:
#             max=i
#     return max
# print(max_divisor(66))


# #9.Return the first prime number greater than n
# def prime(n):
#     new=n+1
    
#     while  new>0:
#         count=0
#         for i in range(1,new+1,1):
#             if new%i==0:
#                 count+=1
#         if count==2:
#             return new
#         new=new+1
# print(prime(97))
        
        
# #10.Return the sum of all prime numbers between 1 and n whose digit sum is also prime
# def sum(n):
#     sum=0
#     for i in range(1,n+1):
#         count=0
#         for j in range(1,i+1):
#             if i%j==0:
#                 count+=1
#         if count==2:
#             sum=sum+i
#     return sum
# print(sum(79))