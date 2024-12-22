from django.db import models

class Quiz(models.Model):
    quiz_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey('courses.Course', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    total_marks = models.IntegerField()

    def __str__(self):
        return self.title

class QuizQuestion(models.Model):
    question_id = models.AutoField(primary_key=True)
    quiz_id = models.ForeignKey('quizzes.Quiz', on_delete=models.CASCADE)
    question_text = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    option_d = models.CharField(max_length=255)
    correct_option = models.CharField(max_length=1)

    def __str__(self):
        return self.question_text
