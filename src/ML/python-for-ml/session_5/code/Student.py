class STUDENT:
    _id_counter = 1

    def __init__(self,student_name):
        self.student_id = STUDENT._id_counter
        STUDENT._id_counter+=1
        self.name = student_name
        self.grades = {}
        self.enrolled_courses = []
    # def __str__(self):
    #     return f"Student Id {self.student_id}, Name: {self.name}, Grades: {(self.grades)}"
    
    def __repr__(self):
        return f"Student Id {self.student_id}, Name: {self.name}, Grades: {(self.grades)},  Enrolled courses: {self.enrolled_courses}" 

    def add_grade(self,course_id,grade):
        self.grades[course_id]= grade

    def enroll_in_course(self, course):
        self.enrolled_courses.append(course)
        print("course enrolled done!.")
