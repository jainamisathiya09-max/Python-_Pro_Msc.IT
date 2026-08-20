def display_report(students):

    print("-" * 60)
    print("              STUDENT RANK REPORT")
    print("-" * 60)

    print("Rank  Roll No  Name       Total  Percentage  Grade")

    print("-" * 60)

    for student in students:
        print(student["rank"], "   ",
              student["rollno"], "     ",
              student["name"], "     ",
              student["total"], "     ",
              student["percentage"], "      ",
              student["grade"])

    print("-" * 60)