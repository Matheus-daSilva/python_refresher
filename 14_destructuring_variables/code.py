x, y = 5, 11

print(x, y)

# -------------------------------------------------------

student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

print(list(student_attendance.items()))

for student, attendance in student_attendance.items():
    print(student, attendance)

# -------------------------------------------------------

people = [("Bob", 42, "Mechanic"), ("James", 24, "Artist"), ("Harry", 32, "Lecturer")]

for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession: {profession}")

# -------------------------------------------------------

person = ("Bob", 42, "Mechanic")
name, _, profession = person # _ indica que a variável não será usada

print(name, profession)

# -------------------------------------------------------

head, *tail = [1, 2, 3, 4, 5] # * atribui as demais variáveis a tail
print(head)
print(tail)