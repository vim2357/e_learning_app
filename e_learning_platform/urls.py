from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Административная панель
    path('admin/', admin.site.urls),

    # Роуты для моделей
    path('courses/', include('courses.urls')),
    path('enrollments/', include('enrollments.urls')),
    path('payments/', include('payments.urls')),
    path('reviews/', include('reviews.urls')),
    path('lessons/', include('lessons.urls')),
    path('quizzes/', include('quizzes.urls')),
    path('quiz-questions/', include('quizzes.urls')),  # Роут для quiz questions

    # Роуты API
    path('api/courses/', include('courses.urls')),
    path('api/enrollments/', include('enrollments.urls')),
    path('api/payments/', include('payments.urls')),
    path('api/reviews/', include('reviews.urls')),
    path('api/lessons/', include('lessons.urls')),
    path('api/quizzes/', include('quizzes.urls')),
    path('api/quiz-questions/', include('quizzes.urls')),  # Quiz Questions API
    path('api/users/', include('users.urls')),
]
