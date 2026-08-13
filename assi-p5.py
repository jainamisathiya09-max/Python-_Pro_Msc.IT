n=int(input("Enter number:"))
students=[]
for i in range(n):
    rollno=int(input("Enter student rollno:"))
    name=input("Enter student name:")

    marks=[]
    for j in range(5):
        m=int(input("Enter student 5 subject mark:"))
        print(m)
        marks.append(m)

    total=sum(marks)
    print("Total is:",total)
    percentage=total/5
    print("Percentage is:",percentage)

    if percentage>=90:
        grade="A+"
    elif percentage>=80:
        grade="A"
    elif percentage>=70:
        grade="B"
    elif percentage>=60:
        grade="C"
    elif percentage>=50:
        grade="D"
    else :
        print("Student is fail")
    print("Grade is:",grade)

    student={"rollno":rollno,
            "name":name,
            "marks":marks,
            "total":total,
            "percentage":percentage,
            "grade":grade}

    students.append(student)
students.sort(key=lambda a:a["total"],reverse=True)
rank=1

for i in range(len(students)):
    if i>0 and students[i]["total"]==students[i-1]["total"]:
        students[i]["rank"]=students[i-1]["rank"]
    else:
        students[i]["rank"]=rank
        rank +=1

for s in students:
    print("Roll No :", s["rollno"])
    print("Name :", s["name"])
    print("Marks :", s["marks"])
    print("Total :", s["total"])
    print("Percentage :", s["percentage"])
    print("Grade :", s["grade"])
    print("Rank :", s["rank"])
