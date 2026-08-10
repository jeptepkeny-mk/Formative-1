from typing import Literal
#might not be necessary
SUBJECT_NAME= Literal["Communication for impact", "E leadership", "Data and decisions", "Projects"]

class Subject:
    def __init__(self, sub_name: SUBJECT_NAME):
        self.sub_name = sub_name


# Find a way to store all subjects in this subjects module