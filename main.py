from exam import Exam
from homework import Homework
from datetime import datetime, timedelta

homework_list = []
exam_list=[]

program_is_on=True

#functions
def add_homework():
    homework = Homework()
    homework_list.append(homework)

def add_exam():
    exam=Exam()
    exam_list.append(exam)

def list_assignment():
    for homework in homework_list:
        print(homework)
    for exam in exam_list:
        print(exam)

def filter_by_month(homeworks, exams, month):
    homework_results = [
        homework for homework in homeworks
        if homework.due_date.month == month
    ]

    exam_results = [
        exam for exam in exams
        if exam.due_date.month == month
    ]

    return homework_results, exam_results

def summary(homeworks, exams):
    assignments = homeworks + exams

    total_assignments = len(assignments)

    total_homeworks = len(homework_list)
    completed_homeworks = sum(
        homework.completed for homework in homework_list
    )
    pending_homeworks = total_homeworks - completed_homeworks

    total_exams = len(exam_list)
    completed_exams = sum(
        exam.completed for exam in exam_list
    )
    pending_exams = total_exams - completed_exams

    today = datetime.today()

    next_7_days = sum(
        today <= assignment.due_date <= today + timedelta(days=7)
        for assignment in assignments
        if not assignment.completed
    )

    next_30_days = sum(
        today <= assignment.due_date <= today + timedelta(days=30)
        for assignment in assignments
        if not assignment.completed
    )

    print("\nASSIGNMENT SUMMARY")
    print(f"Total assignments: {total_assignments}")

    print("\nHomework")
    print(f"    Total: {total_homeworks}")
    print(f"    Completed: {completed_homeworks}")
    print(f"    Pending: {pending_homeworks}")

    print("\nExams")
    print(f"    Total: {total_exams}")
    print(f"    Completed: {completed_exams}")
    print(f"    Pending: {pending_exams}")

    print("\nUpcoming")
    print(f"    Next 7 days: {next_7_days}")
    print(f"    Next 30 days: {next_30_days}")

    print("\n\n")

def mark_assignment_as_completed(homeworks, exams):
    assignments = homeworks + exams

    for i, assignment in enumerate(assignments, start=1):
        status = "Completed" if assignment.completed else "Pending"
        print(f"{i}. {assignment.title} - {status}")

    decision = int(input("Choose an assignment: "))

    assignments[decision - 1].mark_as_complete()

def exit_program():
    print("Goodbye!")

#dictionary of functions
print("Menu")
menu_dict={1:add_homework,2:add_exam, 3:list_assignment,
           4:filter_by_month,5:summary,6:mark_assignment_as_completed,
           0: exit_program}

while program_is_on:
    for key, value in menu_dict.items():
        print(f"{key}: {value}")

    choice=int(input("Enter your choice(answer should be in form of integer): "))

    if choice in menu_dict:
        menu_dict[choice]()
    else:
        print("Invalid input")

    if choice == 0:
        exit_program()
        break
