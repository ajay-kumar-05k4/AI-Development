import json

students = [
    {"id": 1, "name": "Ajai", "marks": 85},
    {"id": 2, "name": "Ravi", "marks": 90},
    {"id": 3, "name": "Sita", "marks": 78}
]

with open("new_student.json", "w") as file:
    json.dump(students, file, indent=4)
