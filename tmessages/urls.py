from django.urls import path

from tmessages.views import MessageDetailView

urlpatterns = [
    path('<int:id>/info/', MessageDetailView.as_view(), name='message-detail'),
    # path('<int:id>/', MessageUpdateView.as_view(), name='message-edit'),
]
