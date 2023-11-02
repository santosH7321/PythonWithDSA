math_marks = int(input("Enter your math marks:"))
eng_marks = int(input("Enter your english marks:"))

#if both are more than 80, print A grade
if eng_marks >= 80 and math_marks >=80 :
    print("Your grade is: A")
elif eng_marks >= 80 or math_marks >= 80:
    print("Your grade is B")
else:
    print("You are just qualified: ")