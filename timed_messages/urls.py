from django.urls import path

from timed_messages.views import LessonTimedMessageListView, LessonTimedMessageCreateView, LessonTimedMessageDeleteView, \
    DailyLessonTimedMessageListView, DailyLessonTimedMessageCreateView, DailyLessonTimedMessageDeleteView

urlpatterns = [
    path('<int:id>/lesson/', LessonTimedMessageListView.as_view(), name='lesson-timed-message-list'),
    path('<int:id>/lesson/new/', LessonTimedMessageCreateView.as_view(), name='lesson-timed-message-create'),
    path('<int:id>/lesson/<int:tmid>/delete/', LessonTimedMessageDeleteView.as_view(), name='lesson-timed-message'
                                                                                            '-delete'),

    path('<int:id>/daily_lesson/', DailyLessonTimedMessageListView.as_view(), name='daily-lesson-timed-message-list'),
    path('<int:id>/daily_lesson/new/', DailyLessonTimedMessageCreateView.as_view(), name='daily-lesson-timed-message'
                                                                                         '-create'),
    path('<int:id>/daily_lesson/<int:tmid>/delete/', DailyLessonTimedMessageDeleteView.as_view(), name='daily-lesson'
                                                                                                       '-timed'
                                                                                                       '-message-delete'),
]
