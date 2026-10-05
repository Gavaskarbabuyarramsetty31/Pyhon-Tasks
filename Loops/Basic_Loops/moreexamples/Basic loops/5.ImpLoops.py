#1.Find whether a number is Prime.
n=int(input("enter the number :"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("Not Prime")
    



#2.Find the sum of digits of a number.
n=input("enter the number :")
output=0
for i in n:
    output+=int(i)
print(output)
#2nd method:
n=int(input("enter the number"))
count=0
while n>0:
    digit=n%10
    count+=digit
    n=n//10
print(count)


#3.Reverse a number.
n=int(input("enter the number"))
count=0
while n>0:
    digit=n%10
    count=count*10+digit
    n=n//10
print(count)



    # 4. Palindrome Number ⭐⭐⭐⭐

n=int(input("enter the number :"))
original=n
reverse=0
while n>0:
    digit=n%10
    reverse=reverse*10+digit
    n=n//10
if reverse == original:
    print ("Palindrom")
else :
    print("Not Palindrom")





