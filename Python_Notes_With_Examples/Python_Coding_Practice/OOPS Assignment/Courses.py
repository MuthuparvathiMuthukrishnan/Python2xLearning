class Course:
    courseName=None
    courseSubject=None
    courseId=0
    courseTeacher=None

    def getCourseName(self):
        print("Getting course name")

    def getcourseSubject(self):
        print("Getting course subject")

    def getcourseId(self):
        print("Getting course id")

    def getcourseTeacher(self):
        print("Getting course teacher")

science=Course()
science.getCourseName()
science.getcourseId()
science.getcourseTeacher()
science.getcourseSubject()

history=Course()
history.getcourseId()
