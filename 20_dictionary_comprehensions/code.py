users = [
    (0, "Bob", "password"),
    (1, "Rolf", "bob123"),
    (2, "Jose", "longp4assword"),
    (3, "username", "1234"),
]

username_mapping = {user[1]: user for user in users}

username_input = input("Enter your username: ")
password_input = input("Enter your password: ")

_, username, password = username_mapping[username_input]

if password_input == password:
    print("Your deails are correct")
else:
    print("Your details are wrong")

# --------------------------------------------------------------
student = [
    {"name": "Marcia", "grades": (6, 7, 5)},
    {"name": "Jose", "grades": (4, 8, 6)}
]

def average_grade_all_students(student_list):
    total = 0
    count = 0

    for student in student_list:
        total += sum(student["grades"])
        count += len(student["grades"])

    return total / count

average_grade = average_grade_all_students(student)

print(average_grade)