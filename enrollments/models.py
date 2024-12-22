from django.db import models
from users.models import User
from courses.models import Course

class Enrollment(models.Model):
    enrollment_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    course_id = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    enrollment_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.user_id.username} - {self.course_id.title}"

class UserProgress(models.Model):
    progress_id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE)
    course_id = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    completed_lessons = models.IntegerField()
    quiz_scores = models.JSONField()

    def __str__(self):
        return f"{self.user_id.username} - {self.course_id.title}"
