# Create a variable called student, with a dictionary.
# The dictionary must contain three keys: 'name', 'school', and 'grades'.
# The values for each must be 'Jose', 'Computing', and a tuple with the values 66, 77, and 88.
student = {
    'name': 'Jose',
    'school': 'Computing',
    'grades': (66, 77, 88)
}

# Assume the argument, data, is a dictionary.
# Modify the grades variable so it accesses the 'grades' key of the data dictionary.
def average_grade(data):
    grades = data['grades']  # returning keyValue as (66, 77, 88)
    return sum(grades) / len(grades) # simple maths


# Implement the function below
# Given a list of students (a list of dictionaries), calculate the average grade received on an exam, for the entire class
# You must add all the grades of all the students together
# You must also count how many grades there are in total in the entire list
def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        # Implement here
        grades = student['grades'] # Access each student's grades
        total += sum(student['grades']) # Add the sum of grades to total
        count += len(student['grades']) # Count the total number of grades
    return total / count # Return the average, guard against division by zero