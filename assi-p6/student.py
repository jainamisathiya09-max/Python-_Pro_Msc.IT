def get_student_data():
    students = []

    n = int(input("Enter number of students: "))

    for i in range(n):
        print("\nEnter details of student", i + 1)

        roll_no = int(input("Enter Roll No: "))
        name = input("Enter Name: ")

        marks = []

        for j in range(5): 
            print("Enter Subject", j + 1, "marks:") 
            m = int(input()) 
            marks.append(m)
        """for j in range(5):
            m = int(input("Enter Subject " + str(j + 1) + " marks: "))
            marks.append(m)
        """
        total = sum(marks)
        percentage = total / 5

        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        student = {
                "rollno": roll_no,
                "name": name,
                "marks": marks,
                "total": total,
                "percentage": percentage,
                 "grade": grade
            }

        students.append(student)

    return students