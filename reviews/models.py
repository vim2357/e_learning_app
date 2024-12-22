from django.db import models

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    course_id = models.ForeignKey('courses.Course', on_delete=models.CASCADE, related_name='course_reviews_alt')
    user_id = models.ForeignKey('users.User', on_delete=models.CASCADE, related_name='user_reviews')
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review by {self.user_id} for {self.course_id}"
