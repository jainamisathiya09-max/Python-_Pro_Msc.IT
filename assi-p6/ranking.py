def generate_rank(students):

    students.sort(key=lambda student: student["total"], reverse=True)

    rank = 1

    for i in range(len(students)):

        if i > 0 and students[i]["total"] == students[i - 1]["total"]:
            students[i]["rank"] = students[i - 1]["rank"]
        else:
            students[i]["rank"] = i + 1

    return students