from django.urls import path

from lessons.views import LessonListView, LessonCreateView, LessonUpdateView, LessonDeleteView

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson-list'),
    path('new/', LessonCreateView.as_view(), name='lesson-create'),
    path('<int:id>/', LessonUpdateView.as_view(), name='lesson-update'),
    path('<int:id>/delete/', LessonDeleteView.as_view(), name='lesson-delete')
]
