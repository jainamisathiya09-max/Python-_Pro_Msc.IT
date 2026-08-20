from student import get_student_data
from ranking import generate_rank
from report import display_report


students = get_student_data()

students = generate_rank(students)

display_report(students)