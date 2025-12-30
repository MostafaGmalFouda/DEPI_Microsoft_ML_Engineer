class COURSE:
    _id_counter = 1

    def __init__(self,name):
        self.course_id = COURSE._id_counter
        COURSE._id_counter+=1
        self.course_name = name
        self.enrolled_students = []

    def __repr__(self):
        return f"Course ID: {self.course_id}, Name: {self.course_name}, Enrolled: {len(self.enrolled_students)}"
    
    def enroll_student(self,sutdent_name):
        if sutdent_name not in self.enrolled_students:
            self.enrolled_students.append(sutdent_name)
            print("student enrolled successfully!.")
        else:
            print("student already enrolled!.")
            
    def remove_student(self,student_name):
        for i in range (len(self.enrolled_students)):
            if self.enrolled_students[i] == student_name:
                del self.enrolled_students[i]
                print("Removed done!.")
            else:
                print("Name not found!.")

        # if student_name in self.enrolled_students:
        #     self.enrolled_students.remove(student_name)
        #     print("Removed done!.")
        # else:
        #     print("Name not found!.")
