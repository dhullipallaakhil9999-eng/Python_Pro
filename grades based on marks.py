marks=int(input("Enter marks : "));
if marks < 0 and marks > 100:
    print("Invalid marks");
elif marks >= 95:
    print("Grade A");
elif marks >= 80:
    print("Grade B");
elif marks >=70:
    print("Grade C");
elif marks >= 60:
    print("Grade D");
elif marks >=40:
    print("Grade E");
else:
    print("Fail");