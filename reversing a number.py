num=int(input("Enter number : "));
reverse=0;
while num>0:
    digits=num%10
    reverse=reverse*10+digits
    num//=10;
print("reversed number = ",reverse)