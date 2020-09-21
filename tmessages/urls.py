from django.urls import path

from tmessages.views import MessageDetailView, MessageUpdateView

urlpatterns = [
    path('<int:id>/', MessageUpdateView.as_view(), name='message-edit'),
    path('<int:id>/info/', MessageDetailView.as_view(), name='message-detail')
]
