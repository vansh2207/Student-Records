import pandas as pd
import os

def add_student_record(student_records, num_subjects):
    student_name = input("Enter student's name: ")
    student_records[student_name] = {}  
    for subject in range(num_subjects):
        while True:
            try:
                grade = float(input(f"Enter grade for subject {subject + 1}: "))
                student_records[student_name][f"Subject {subject + 1}"] = grade
                break
            except ValueError:
                print("Invalid input. Please enter a number for the grade.")
    
    percentage = calculate_percentage(list(student_records[student_name].values()))
    grade_letter = calculate_grade(percentage)
   
    student_records[student_name]["percentage"] = percentage
    student_records[student_name]["grade"] = grade_letter
    print("Student record added successfully.")

def display_student_records(student_records):
    if not student_records:
        print("No student records found.")
        return

    for student_name, student_data in student_records.items():
        print(f"\nStudent: {student_name}")
        for subject, grade in student_data.items():
            if subject != "percentage" and subject != "grade": 
                print(f"{subject}: {grade}")
        print(f"Percentage: {student_data['percentage']}%")
        print(f"Grade: {student_data['grade']}")

def calculate_percentage(grades):
    total_marks = sum(grades)
    num_subjects = len(grades)
    return (total_marks / (num_subjects * 100)) * 100

def calculate_grade(percentage):
    if percentage >= 90:
        return "A"
    elif 80 <= percentage < 90:
        return "B"
    elif 70 <= percentage < 80:
        return "C"
    elif 60 <= percentage < 70:
        return "D"
    else:
        return "F"

def main():
    student_records = {}
    num_subjects = int(input("Enter the number of subjects: "))
    num_students = int(input("Enter the number of students: "))

    for _ in range(num_students):
        add_student_record(student_records, num_subjects)

    while True:
        print("\nMenu:")
        print("1. Add Student Record")
        print("2. Display All Student Records")
        print("3. Save Student Records to Excel")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_student_record(student_records, num_subjects)
        elif choice == 2:
            display_student_records(student_records)
        elif choice == 3:
            save_to_excel(student_records)
            os.startfile("Records.xlsx")
        elif choice == 4:
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")
        save_to_excel(student_records)

def save_to_excel(student_records):
    df = pd.DataFrame.from_dict(student_records, orient='index')
    df.to_excel("Records.xlsx")
    print("Student records saved to Excel file.")

if __name__ == "__main__":
    main()
