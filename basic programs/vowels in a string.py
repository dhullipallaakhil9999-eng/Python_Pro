str=str(input("Enter a string : "));
count=0;
for ch in str:
    if ch.lower() in "aeiou":
        count+=1;
print("No.of vowels : ",count)