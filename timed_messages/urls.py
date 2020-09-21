from django.urls import path

from timed_messages.views import LessonTimedMessageListView, LessonTimedMessageCreateView, LessonTimedMessageDeleteView

urlpatterns = [
    path('<int:id>/lesson/', LessonTimedMessageListView.as_view(), name='lesson-timed-message-list'),
    path('<int:id>/lesson/new/', LessonTimedMessageCreateView.as_view(), name='lesson-timed-message-create'),
    path('<int:id>/lesson/<int:tmid>/delete/', LessonTimedMessageDeleteView.as_view(), name='lesson-timed-message'
                                                                                            '-delete'),

    # path('daily_lesson/', DailyLessonTimedMessageListView.as_view(), name='daily-lesson-timed-message-list'),
    # path('daily_lesson/new/', DailyLessonTimedMessageCreateView.as_view(),
    # name='daily-lesson-timed-message-create'), path('daily_lesson/<int:id>/',
    # DailyLessonTimedMessageUpdateView.as_view(), name='daily-lesson-timed-message-update'),
    # path('daily_lesson/<int:id>/delete/', DailyLessonTimedMessageDeleteView.as_view(), name='daily-lesson-timed'
    # '-message-delete')
]