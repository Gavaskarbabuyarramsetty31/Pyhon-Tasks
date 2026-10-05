# # #1. Largest Prime Factor
# # Example:
# # Input:  84
# # Output: 7
# # Because:
# # 84 = 2 × 2 × 3 × 7

# def largest_prime_factor(n):
#     largest_factor=0
#     for i in range(1,n+1,1):
#         if n%i==0:
#             count=0
#             for j in range(1,i+1):
#                 if i%j==0:
#                     count+=1
#             if count==2 and largest_factor<i:
#                 largest_factor=i
#     return largest_factor
# print(largest_prime_factor(84))
                
                
                
# # 2. Strong Number
# # Write a function that checks whether n is a Strong Number.
# # A number is Strong if the sum of the factorials of its digits equals the number.
# # Example:
# # 145
# # Because:
# # 1! + 4! + 5!
# # = 1 + 24 + 120
# # = 145

# def strong_number(n):
#     new=n
#     sum=0
#     while n>0:
#         product=1
#         ld=n%10
#         for i in range(1,ld+1):
#             product=i*product
#         sum+=product
#         n=n//10
#     if new==sum:
#         return True
#     else:
#         return False
# print(strong_number(145))
            


# # 3. Find the Second Largest Digit
# # Write a function that returns the second largest distinct digit in a number.
# # Example:
# # Input: 583921
# # Output: 8
# # Another:
# # Input: 987799
# # Output: 8
# # You must handle cases where the largest digit occurs multiple times.

# def second_largest_num(n):
#     new=n
#     first=0
#     second=0
#     while n>0:
#         ld=n%10
#         if ld>first:
#             second=first
#             first=ld
#         elif ld>second and ld!=first:
#             second=ld
#         n=n//10
#     return second
# print(second_largest_num(5973921))
        
            
# 4. Digit Frequency Without Lists/Strings
# Write a function that returns how many times the most frequently occurring digit appears.
# Example:
# Input: 12233341
# Output: 3
# Because:
# 1 → 2 times
# 2 → 2 times
# 3 → 3 times
# 4 → 1 time
# So the answer is 3.


# def frequency(n):
    