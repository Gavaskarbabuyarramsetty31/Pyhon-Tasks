# # #1.Find the sum of digits in a given number.
# #     Example: 738 → 7 + 3 + 8 = 18
# n=82198
#new=n
# sum=0
# while n!=0:
#     ld=n%10
#     sum=sum+ld
#     n=n//10
# print(f"The sum of digits in {new} : {sum}")



# # 2.Find the average of digits in a given number.
# #      Example: 624 → (6 + 2 + 4) / 3 = 4
# n=624
# new=n

# count=0
# sum=0
# while n!=0:
#     ld=n%10
#     sum=sum+ld
#     count=count+1
#     n=n//10
# print(f"Average of digits in {new } : {sum/count}")


# # 3.Find the sum of the first digit and the last digit of a given number.
# #      Example: 936 → 9 + 6 = 15
# n=5899754
# last=n%10
# first=0
# while n>0:
#     ld=n%10
#     if n<10:
#         first=ld
#     n=n//10
# print(f"sum of first and last digit is {last+first}")

        
# # 4.Find the average of digits that are divisible by 5 in a given number.
# #      Example: 12575 → Divisible by 5 digits: 5, 5, 5 → Average = (5 + 5 + 5) / 3 = 5
# n=1257535465
# new=n
# sum=0
# count=0
# while n!=0:
#     ld=n%10
#     if ld%5==0:
#         sum=sum+ld
#         count+=1
#     n=n//10
# average=sum/count
# print(f"average of digits that are divisible by 5 in  {new} is : {average}")


# # 5.Find the difference between the largest digit and the smallest digit in a given number.
# #      Example: 58321 → Largest = 8, Smallest = 1 → Difference = 8 - 1 = 7
# n=37348593
# large=0
# small=9
# while n!=0:
#     ld=n%10
#     if ld>large:
#         large=ld
#     elif ld<small:
#         small=ld
#     n=n//10
# print(f"the difference between {large} and {small} = {large-small}")




