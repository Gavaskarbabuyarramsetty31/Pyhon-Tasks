
# 🔴 Level 4 – Nested Loops (16–20)
# 16. Print the following pattern.
# *
# **
# ***
# ****
# *****
for i in range(1,6):
    print(i*"*")
    

    
#17. Print this pattern.
# *****
# ****
# ***
# **
# *

for i in range(5,0,-1):
    print(i*"*")


# 18. Print the following pattern.
# 1
# 12
# 123
# 1234
# 12345
for i in range(1,6):
    for j in range(1,i+1):     #(here we need to set range correctly)
        print(j,end="")
    print()
    
#19. Print the following pattern.
# A
# AB
# ABC
# ABCD
# ABCDE
list=["A","B","c","D","E"]
for i in range(1,6):
    for j in range(i):
        print(chr(65+j),end="")        #here chr(65)=A,chr(66)=B
    print()
    

# 20. Print this multiplication table.
# 1 x 1 = 1
# 1 x 2 = 2
# ...
# 1 x 10 = 10

# 2 x 1 = 2
# ...
# 10 x 10 = 100

for i in range(1,11):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)
    print()