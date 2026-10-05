#11. Count how many even numbers are between 1 and 100.:
count=0
for i in range(1,101):
    if i%2==0:
        count+=1
print(count)

#12. Count how many odd numbers are between 1 and 100.
count=0
for i in range(1,100):
    if i%2!=0:
        count+=1
print(count)

#13. Find the largest number from five numbers entered by the user.
a=int(input("enter the num 1 :"))
b=int(input("enter the num 2 :"))
c=int(input("enter the num 3 :"))
d=int(input("enter the num 4 :"))
e=int(input("enter the num 5 :"))
numbers=[a,b,c,d,e]
max_num= numbers[0]        #here numbers[0]=a
for i in list:
    if max_num<i:
        max_num=i
print(" Max number :",max_num)

#14. Reverse the numbers from 100 to 1.
for i in range(100,1,-1):
    print(i,end=",")


#15. Print the square of numbers from 1 to 10.
for i in range(1,11):
    k=i*i
    print(k,end=",")