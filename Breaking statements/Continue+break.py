# # 1.Print 1–50, skip multiples of 3, stop at 40.
# for i in range(1,51,1):
#     if i%3==0:
#         continue
#     print(i)
#     if i==40:
#         break
    
# #2.Print odd numbers, skip evens, stop at the first multiple of 7.
# i=1
# while i>0:
#     if i%2==0:
#         i=i+1
#         continue
#     print(i)
#     if i%7==0:
#         break
#     i=i+1

# #3.Extract 5830421, skip odd digits, stop at 0.
# n=5830421
# while n>0:
#     ld=n%10
#     if ld%2!=0:
#         n=n//10
#         continue
#     if ld==0:
    
#         break
#     print(ld)
#     n=n//10
    
# #4.Extract 8325147, print digits until 5.
# n=8325147
# while n>0:
#     ld=n%10
#     if ld==5:
#         break
#     print(ld)
#     n=n//10

# #5.Search from 51, skip non-multiples of 9, stop at the first multiple of 9.
# i=51
# while i>1:
#     if i%9!=0:
#         i=i+1
#         continue
#     if i%9==0:
#         print(i)
#         break
    
#     i=i+1