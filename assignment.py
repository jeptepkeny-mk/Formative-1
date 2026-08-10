import subjects
from datetime import datetime

ASSIGNMENT_TYPE=["homework","exam"]

class Assignment(subjects.Subject):
    #creates assignment object in the constructor as well as validating all inputs
    def __init__(self):
        sub_name = input("Enter subject name: ")
        super().__init__(sub_name)


        self.title = input("Enter assignment title: ")
        self.completed=False
        #validates inputs starting with assignment score
        while True:
            try:
                self.assign_score = float(input("Enter assignment score: "))

                if self.assign_score < 0:
                    print("Score cannot be negative.")
                    continue

                break

            except ValueError:
                print("Please enter a valid number.")


        #maximum score
        while True:
            try:
                self.max_score = float(input("Enter maximum score: "))

                if self.max_score <= 0:
                    print("Maximum score must be greater than 0.")
                    continue

                break

            except ValueError:
                print("Please enter a valid number.")
        #due dates
        while True:
            self.due_date = input("Enter due date (YYYY-MM-DD): ")

            try:
                datetime.strptime(self.due_date, "%Y-%m-%d")
                break
            except ValueError:
                print("Invalid date. Please use YYYY-MM-DD.")



    #allows me to print all the assignments, rather than memory locations
    def __str__(self):
        return (f"Subject: {self.sub_name},\n"
                f"Title: {self.title},\n"
                f"Score: {self.assign_score}/{self.max_score},\n"
                f"Due Date: {self.due_date},\n"
                f"Type: {self.atype}\n\n")

    @classmethod
    def filter_assignment(cls, assignments, assignment_type):
        return [
            a for a in assignments
            if a.atype == assignment_type
        ]

    def mark_as_completed(self):
        self.completed = True