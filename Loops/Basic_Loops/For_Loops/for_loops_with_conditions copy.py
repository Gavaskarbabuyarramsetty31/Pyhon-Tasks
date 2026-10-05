# #1.display even numbers in the range of 1 to 5
# n=5
# for i in range(1,n+1,1):
#     if (i%2==0):
#         print(i)
        
# #dispay odd in rNge of 15 to 11

# print("with loop:")
# s=15
# n=11
# for i in range(s,n-1,-1):
#     if(i%2!=0):
#         print(i)
        
        
# # without loop:
# print("without loop:")
# if(15%2!=0):
#     print(15)
# if(14%2!=0):
#     print(14)    
# if(13%2!=0):
#     print(13)

# if(12%2!=0):
#     print(12)
# if(11%2!=0):
#     print(11)


# #divisible of 5 in the range of 5 to 10:
# #without loop
# print("without loop")
# if(5%5==0):
#     print(5)
# if(6%5==0):
#     print(6)
# if(7%5==0):
#     print(7)
# if(8%5==0):
#     print(8)
# if(9%5==0):
#     print(9)
# if(10%5==0):
#     print(10)
    
# print("with loop :")
# s=5
# n=10
# for i in range(s,n+1,1):
#     if(i%5==0):
#         print(i)



#count the even numbers in the range of 1 to 10
# count=0
# for i in range (1,11,1):
#     if(i%2==0):
#         count+=1
# print(f'The count of Even Numbers = {count}')


# #display the sum of odd numbers in the range of 15 to 5
# sum=0
# for i in range(5,11,1):
#     if(i%2!=0):
#         sum=sum+i
        
# print(f"The sum of odd numbers in the range of 5 to 10 is = {sum}")

# #display the sum of odd numbers in the range of 15 to 5
# sum=0
# for i in range(15,4,-1):
#     if(i%2!=0):
#         sum=sum+i        
# print(f"The sum of odd numbers in the range of 15 to 5 is = {sum}")




# #print the factors for n
# n=88
# print(f"The factors of {n} :")
# for i in range(1,n+1,1):
#     if(n%i==0): 
#         print(i)



# #count the factors of a number
# n=89
# count=0

# for i in range(1,n+1,1):
#     if(n%i==0):
#         count+=1
# print(f"The count of factors of {n} : {count}")       

    
# #find a number is a prime or not?
# n=89
# count=0

# for i in range(1,n+1,1):
#     if(n%i==0):
#         count+=1
# # print(f"The count of factors of {n} : {count}")       
# if (count==2):
#     print(f"{n} it is  prime number ")
# else:
#     print(f"{n} it is not prime number")

# #display the sum of factor if a number
# n=8
# sum=0
# for i in range(1,n+1,1):
#     if(n%i==0):
#         sum+=i
# print(f"sum of factors of {n} : {sum}")

#print the all the prime numbers in the range of 1 to 100:
# g=100
# for i in range(1,g+1,1):
#     count=0
#     for j in range(1,i+1,1):
#         if(i%j==0):
#             count+=1
#     if(count==2):
#         print(i)



#find the number is a perfect  number (when sum of factors excluding itself equal to the original number)
# sum=0
# n=6
# for i in range(1,n,1):
#     if(n%i==0):
#         sum+=i
# if(sum==n):
#     print(f"{n} is a pefect number ")
# else:
#     print("print is not a perfect number")
        