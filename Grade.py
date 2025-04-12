while True:
    grade = input("Enter your grade(A, B, C, D, F): ")
    if grade in ["A", "B", "C", "D", "F"]:
        break
    print("Invalid grade. Please try again.")

    print(f"You entered a valid grade: {grade}")