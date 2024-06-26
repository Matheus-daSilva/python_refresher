friend_ages = {"Rolf": 24, "Adam": 30, "Anne": 27}

print(friend_ages["Adam"])

# --------------------------------------------------

friend_ages["Bob"] = 20 # adiciona um elemento novo no dicionário

print(friend_ages)

# --------------------------------------------------

friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]

print(friends[0]["name"])

# --------------------------------------------------

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

# --------------------------------------------------

attendance_values = student_attendance.values()
print(attendance_values)
print(sum(attendance_values))    