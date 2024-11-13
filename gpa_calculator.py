# Ask for the number of subjects
num_subjects = int(input("How many courses do you want to calculate the GPA for? "))

total_points = 0
total_credit_hours = 0

for i in range(num_subjects):
    GP = str(input(f"Please enter your grade for course {i + 1}: ")).upper()
    CH = int(input(f"Please enter your credit hours for course {i + 1}: "))
    
    # Calculate points based on the grade
    if GP == "A":
        points = 4.0 * CH
    elif GP == "A-":
        points = 3.67 * CH
    elif GP == "B+":
        points = 3.33 * CH
    elif GP == "B":
        points = 3.0 * CH
    elif GP == "B-":
        points = 2.67 * CH
    elif GP == "C+":
        points = 2.33 * CH
    elif GP == "C":
        points = 2.0 * CH
    elif GP == "C-":
        points = 1.67 * CH
    elif GP == "D+":
        points = 1.33 * CH
    elif GP == "D":
        points = 1.0 * CH
    elif GP == "F":
        points = 0 * CH
    else:
        print("Invalid grade entered. Please enter a valid grade.")
        continue  # Skip to the next iteration if the grade is invalid

    total_points += points
    total_credit_hours += CH

# Formula for GPA
GPA = total_points / total_credit_hours if total_credit_hours > 0 else 0
print("Your GPA is ", GPA)
