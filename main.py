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

def grade_summary():
    homework_sum = 0
    exam_sum = 0

    for homework in homework_list:
        score = round(homework.assign_score / homework.max_score, 2)
        homework_sum += score

    if len(homework_list) > 0:
        avg_hw_score = round(homework_sum / len(homework_list), 2)
        print(f"Average homework score: {avg_hw_score}/1.0")
    else:
        print("No homework assignments available.")

    for exam in exam_list:
        score = round(exam.assign_score / exam.max_score, 2)
        exam_sum += score

    if len(exam_list) > 0:
        avg_ex_score = round(exam_sum / len(exam_list), 2)
        print(f"Average exam score: {avg_ex_score}/1.0")
    else:
        print("No exams available.")

#removing arguments from filter by month
def filter_by_month():
    while True:
        try:
            month = int(input("Enter the month number (1-12): "))

            if 1 <= month <= 12:
                break
            else:
                print("Invalid input. Please enter a month between 1 and 12.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    homework_results = [
        homework for homework in homework_list
        if homework.due_date.month == month
    ]

    exam_results = [
        exam for exam in exam_list
        if exam.due_date.month == month
    ]

    print("\nHomework:")
    for homework in homework_results:
        print(homework.title)

    print("\nExams:")
    for exam in exam_results:
        print(exam.title)

def summary():
    assignments = homework_list + exam_list

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

def mark_assignment_as_completed():
    assignments = homework_list + exam_list

    for i, assignment in enumerate(assignments, start=1):
        status = "Completed" if assignment.completed else "Pending"
        print(f"{i}. {assignment.title} - {status}")

    while True:
        try:
            decision = int(input("Choose an assignment: "))

            if 1 <= decision <= len(assignments):
                break
            else:
                print(f"Invalid input. Please choose a number between 1 and {len(assignments)}.")

        except ValueError:
            print("Invalid input. Please enter a number.")

    assignments[decision - 1].mark_as_completed()

def exit_program():
    print("Goodbye!")

#dictionary of functions
#fixing memory addresses
print("Menu")
menu_dict = {
    1: (add_homework, "Add homework"),
    2: (add_exam, "Add exam"),
    3: (list_assignment, "List assignments"),
    4: (filter_by_month, "Filter by month"),
    5: (summary, "Summary"),
    6: (mark_assignment_as_completed, "Mark assignment as completed"),
    7: (grade_summary, "Grade summary"),
    0: (exit_program, "Exit")
}

while program_is_on:
    for key, value in menu_dict.items():
        print(f"{key}: {value[1]}")
    while True:
        try:
            choice=int(input("Enter your choice(answer should be in form of integer): "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")


    if choice == 0:
        exit_program()
        break

    if choice in menu_dict:
        menu_dict[choice][0]()
    else:
        print("Invalid input")


