a=int(input("enter a number"))
rev=0
rem=0
temp=a
while(a != 0):
    rem=a%10
    rev=(rev*10)+rem
    a=a//10
if(temp==rev):
    print("num is palindrome")
else:
    print("not palindrome")