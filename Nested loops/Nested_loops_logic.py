# #print the sum pairs of 5 in the range(1 to 5)
# for i in range(1,6,1):
#     for j in range(1,6,1):
#         if(i+j==5) :
#             print(f"i={i} and j={j}")
        
# #display even numbers in the range (1 to 10):
# for i in range(1,11,1):
#     n=i
#     if(n%2==0):
#         print(n,end=", ")

# # #display odd numbers in the range (1 to 10):
# print("Odd numbers :")
# for i in range(1,11,1):
#     n=i
#     if(n%2!=0):
#         print(n,end=", ")


# #print the multiplication table for each number in the give range()

# for i in range(1,6,1):
#     for j in range(1,11,1):
#         print(f"{i} X {j} = {i*j}")
#     print()


# #display factorials of each number in the given range(1 to 5)

# for j in range(10,16,1):
#     n=j
#     factorial=1
#     for i in range(1,n+1,1):
#         factorial=factorial*i
#     print(f"factorial of {j} = {factorial}")



# # print the print prime number
# print ("Prime numbers in the range of 1 to 100:",end="")
# for j in range(1,101,1):
#     n=j
#     count=0
#     for i in range(1,n+1,1):
#         if(n%i==0):
#             count+=1
#     if count==2:
#         print(n,end=",")


# for j in range(1,10001,1):
    
#     sum=0
#     n=j
#     for i in range(1,n,1):
#         if(n%i==0):
#             sum+=i
#     if(sum==n):
#         print(f"{n} is a pefect number ")
  
  
  
  
# #display palindrom in the range (100,150)
# print("Palindrom in the range of 100 to 150 :")
# for i in range(100,151,1):
#     n=i
#     new=n
#     rev=0
#     while n>0:
#         ld=n%10
#         rev=(rev*10)+ld
#         n=n//10
#     if new==rev :
#         print(new)