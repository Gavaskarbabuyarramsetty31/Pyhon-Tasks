#6. Take a number n from the user and print numbers from 1 to n.:
n=int(input("Enter the number"))
for i in range(1,n+1):
    print(i, end="")
#7. Print the multiplication table of a given number.
n=int(input("Enter the Number :"))
for i in range(11):
    print(f"{n} * {i}=",n*i)
#--->>>8.Find the sum of numbers from 1 to n.:
n=int(input("Enter the number :"))
count=0
for i in range(1,n):
    count+=i
print(count)


#-->>9. Find the factorial of a number.:
n=int(input("enter the number :"))
count=1
for i in range(1,n+1):
    count*=i
print(count)

#10. Count from 1 to n, but print only multiples of 5.:
n=int(input("Enter the number :"))
for i in range(1,n+1):
    if i%5==0:
        print(i,end=",")