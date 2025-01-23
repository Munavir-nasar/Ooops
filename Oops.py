class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def __str__(self):
        return f"{self.course_code}: {self.course_name} ({self.credit_hours} credit hours)"

class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def __str__(self):
        return super().__str__() + f" (Required for major: {self.required_for_major})"

class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def __str__(self):
        return super().__str__() + f" (Elective type: {self.elective_type})"
core_course = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
elective_course = ElectiveCourse("CS202", "Data Structures and Algorithms", 3, "technical")
#
print(core_course)
print(elective_course)

# question 2
import employee as e

emp2 = e.Employee("Munavir", 80000)
print("Employee Name:",emp2.get_name())
print("Employee Salary:",emp2.get_salary())

