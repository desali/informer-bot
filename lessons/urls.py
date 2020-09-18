from django.urls import path

from lessons.views import LessonListView, LessonEditView

urlpatterns = [
    path('', LessonListView.as_view(), name='lesson-list'),
    path('<int:id>/', LessonEditView.as_view(), name='lesson-edit')
]