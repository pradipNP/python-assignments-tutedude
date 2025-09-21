marks = {"Alice": 85,
         "Bob": 89,
         "Charlie": 87
        }

student = input("Enter the student's name: ")

if student in marks:
    print(f"{student}'s marks: {marks[student]}")

else:
    print("Student not found.")