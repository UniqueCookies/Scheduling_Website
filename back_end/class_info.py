from scheduling_website.back_end.teacher import Teacher

# class_type will be an add-on feature for later where two coures need to be combined together.
# grade level indicate which section this course can be taught in
class Course:
    def __init__(self, course_name, teacher_info, class_type, grade_level):
        self.course_name = course_name
        self.teacher_info = teacher_info
        self.class_type = class_type
        self.grade_level = grade_level

    def __str__(self):
        combined_text = "Combined" if self.class_type==1 else "Single"
        return f"Course: {self.course_name}\nTeacher: {self.teacher_info}\nType: {combined_text}\nGrade Level: {self.grade_level}"


