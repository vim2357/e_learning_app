from django.contrib import admin
from .models import Course, Lesson, Review, Category

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Review)
admin.site.register(Category)
