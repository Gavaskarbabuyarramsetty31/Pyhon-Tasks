# # #Sum of Prime Numbers
# # Find the sum of all prime numbers between 20 and 150.

# sum=0
# for i in range(20,151,1):
#     n=i
#     count=0
#     for j in range(1,n+1,1):
#         if(n%j==0):
#             count+=1
#     if(count==2):
#         sum+=n
# print(f"sum of prime numbers {sum}")

# #2 . Average of Perfect Numbers
# # Find the average of all perfect numbers between 1 and 1000.

# main_sum=0
# count=0
# for i in range(1,10000,1):
#     n=i
#     sum=0
#     for j in range(1,n,1):
#         if n%j==0:
#             sum+=j
#     if n==sum:
#         main_sum+=n
#         count+=1
# print(f"Average={main_sum/count}")

# # 3.Leap Years in a Range(Not Nested Loop Logic)
# # Print all leap years between 1900 and 2026.
# for i in range(1900,2027,1):
#     if i%4==0 and i%100!=0:
#         print(i,end=",")

# # #4.Palindrome Numbers
# # Print all palindrome numbers between 100 and 500.
# for i in range(100,501,1):
#     n=i
#     new=n
#     rev=0
#     while n>0:
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     if new==rev:
#         print(new,end=",")

# # #5.Digit Sum = 10
# # Print all numbers between 120 and 850 whose digit sum is exactly 10.

# for i in range(120,851,1):
#     n=i
#     sum=0
#     while n>0:
#         ld=n%10
#         sum+=ld
#         n=n//10
#     if sum==10:
#         print(i,end=",")


# for i in range(1,26,1):
#     for j in range(1,26,1):
#         if (i+j==30):
#             print(f"a={i}, & b={j}")

# #7. Exactly 3 Factors
# # Print all numbers between 10 and 300 that have exactly 3 factors.
# for i in range(10,301,1):
#     n=i
#     count=0
#     for j in range(1,i+1,1):
#         if (n%j==0):
#             count+=1
#     if count==3:
#         print(i,end=",")


# #8. Prime Factors
# # Print the prime factors of every number between 20 and 50.
# for i in range(20,51,1):
#     n=i
#     for j in range(1,i+1,1):
#         if(n%j==0):
#             count=0
#             for k in range(1,j+1,1):
#                 if j%k==0:
#                     count+=1
#             if count==2:
#                 print(f"the prime factors of {i}:{j}")


# 9.Armstrong Numbers
# # Print all Armstrong numbers between 100 and 999.
# for i in range(100,1000,1):
#     n=i
#     new=n
#     count=0
#     sum=0
#     while i>0:
#         ld=i%10
#         count+=1
#         i=i//10
#     while n>0:
#         ld=n%10
#         sum=sum+(ld**count)
#         n=n//10
#     if new==sum:
#         print(f"{new} is Armstrong Number")


# Maximum Factors
# # Find the number between 50 and 150 that has the maximum number of factors.
# main_count=0
# new=0
# for i in range(50,151,1):
#     n=i
#     count=0
#     for j in range(1,n+1,1):
#         if(i%j==0):
#             count+=1
#     if count>main_count:
#         main_count=count
#         new=i
# print(f"the number {new} have highest factors with {main_count} factors")


