number1 = int(input("Enter total number of working days: "))
number2 = int(input("Enter number of days absent: "))
calculate = ((number1 - number2) / number1) * 100  
print("Percentage of attendance is:", calculate)
if calculate >= 75:
    print("You are eligible for the exam.")
else:
    print("You are not eligible for the exam.")