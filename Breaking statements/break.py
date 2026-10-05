# #1.Find the first even digit from the left in 753914286.
# n=753914286
# new=n
# rev=0
# while n>0:
#     ld=n%10
#     rev=rev*10+ld
#     n=n//10
# last=0
# while rev>0:
#     last=rev%10
#     if last%2==0:
#         print(f"the first even digit of {new} is {last}")
#         break
#     rev=rev//10

# # 2.Find the first prime number between 50 and 100.
# for i in range(50,101,1):
#     count=0
#     for j in range(1,i+1,1):
#         if i%j==0:
#             count+=1
#     if count==2:
#         print(f"The first prime number is {i}")
#         break


# #3.Find the first number whose digit sum is 10.
# for i in range(1,10000,1):
#     n=i
#     sum=0
#     while n>0:
#         ld=n%10
#         sum=sum+ld
#         n=n//10
#     if sum==10:
#         print(i)
#         break


# #4.Find the first number with exactly 3 divisors between 1 and 100.
# for i in range(1,101,1):
#     count=0
#     for j in range(1,i+1,1):
#         if i%j==0:
#             count+=1
#     if count==3:
#         print(i)
#         break


# #5.Stop when 3 consecutive odd numbers occur between 1 and 50.
# for i in range(1,51,1):
#     count=0
#     if i%2!=0:
#         count+=1
#     else:
#         count-=1
#     if count==3:
#         print(i)
#         break
#     else:
#         print("There are no 3 consecutive numbers ")

# #6.Find the first palindrome between 10 and 500.
# for i in range(10,501,1):
#     n=i
#     rev=0
#     while n>0:
#         ld=n%10
#         rev=rev*10+ld
#         n=n//10
#     if i==rev:
#         print(i)
#         break

# #7.Find the first perfect number between 1 and 1000.
# for i in range(1,1001,1):
#     sum=0
#     for j in range(1,i,1):
#         if i%j==0:
#             sum+=j
#     if i==sum:
#         print(i)
#         break

# #8.Print the first 5 even numbers.
# i=1
# count=0
# while i>0:
#     if i%2==0:
#         count+=1
#         print(i)
#     i=i+1
#     if count==5:
#         

# #9.Print the first 5 prime numbers.
# i=1
# count=0
# while i>0:
#     c=0
#     for j in range(1,i+1,1):
#         if i%j==0:
#             c+=1
#     i=i+1
#     if c==2:
#         print(i)
#         count+=1
#     if count==5:
    
#         break


# #10.Print the first 3 numbers divisible by 7.
# i=1
# count=0
# while i>0:
#     if i%7==0:
#         count+=1
#         print(i)
#     i=i+1
#     if count==3:
#         break