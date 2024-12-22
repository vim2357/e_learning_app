from django.db import models

class Lesson(models.Model):
    lesson_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    content = models.TextField()
    video_url = models.URLField()

    def __str__(self):
        return self.title
