# class_type will be an add-on feature for later
# where two coures need to be taught at the same time.
# grade level indicate which section this course can be taught in
class Course:
    def __init__(self, course_name, teacher_name, class_type, grade_level):
        self.course_name = course_name
        self.teacher_name = teacher_name
        self.class_type = class_type
        self.grade_level = grade_level

    def __str__(self):
        combined_text = "Combined" \
            if self.class_type == 1 else "Single"
        return f"Course: {self.course_name}\n" \
               f"Teacher: {self.teacher_name}\n" \
               f"Type: {combined_text}\nGrade Level: {self.grade_level}"
