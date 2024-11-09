# Student Record Management System

## Overview

This project is a Python-based student record management system that allows users to add student records, calculate their grades, and save the data to an Excel file. The system supports adding records for multiple subjects and displaying student details along with their grades and percentages.

## Features

1. **Add Student Record**  
   - Users can add a new student record with their grades for each subject.
   - The system will calculate the student's percentage and assign a grade based on the percentage.

2. **Display All Student Records**  
   - Displays the records for all students, including their grades for each subject, percentage, and grade.

3. **Save Student Records to Excel**  
   - Saves all student records to an Excel file (`Records.xlsx`) for easy sharing and archiving.

4. **Exit Program**  
   - Allows the user to exit the program safely.

## Requirements

- **Python 3.x**
- **Pandas Library**: You need the `pandas` library for handling and saving student records to Excel.
  You can install it via pip:
  ```bash
  pip install pandas
  ```
- **Openpyxl Library**: This is required for saving Excel files.
  You can install it via pip:
  ```bash
  pip install openpyxl
  ```

## How to Use

1. **Run the Program**:  
   - Execute the Python script using your preferred IDE or directly from the terminal:
   ```bash
   python student_record_system.py
   ```

2. **Input Details**:  
   - First, enter the number of subjects and the number of students.
   - For each student, input their name and the grade for each subject.
   - The system will calculate the student's percentage and grade automatically.

3. **Menu Options**:
   - **Option 1: Add Student Record** – Add a new student record.
   - **Option 2: Display All Student Records** – View all student records along with their grades and percentage.
   - **Option 3: Save Student Records to Excel** – Save the records to an Excel file.
   - **Option 4: Exit** – Exit the program.

4. **View Excel File**:  
   After saving the records, the Excel file `Records.xlsx` will be opened automatically.

## Code Explanation

- **add_student_record()**: Prompts the user to enter the student's name and grades for each subject, calculates the percentage and grade, and stores the data in a dictionary.
- **display_student_records()**: Displays all stored student records, including grades, percentage, and grade letter.
- **calculate_percentage()**: Calculates the percentage based on the grades entered.
- **calculate_grade()**: Assigns a grade letter based on the percentage.
- **save_to_excel()**: Converts the student records dictionary into a Pandas DataFrame and saves it to an Excel file (`Records.xlsx`).
- **main()**: The main loop of the program that provides the user with options and handles user input.
