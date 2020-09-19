from django.urls import path

from daily_lessons.views import DailyLessonDeleteView, DailyLessonListView, DailyLessonCreateView, DailyLessonUpdateView

urlpatterns = [
    path('', DailyLessonListView.as_view(), name='daily-lesson-list'),
    path('new/', DailyLessonCreateView.as_view(), name='daily-lesson-create'),
    path('<int:id>/', DailyLessonUpdateView.as_view(), name='daily-lesson-update'),
    path('<int:id>/delete/', DailyLessonDeleteView.as_view(), name='daily-lesson-delete')
]
