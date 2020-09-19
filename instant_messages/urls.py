from django.urls import path

from instant_messages.views import InstantMessageListView, InstantMessageCreateView

urlpatterns = [
    path('', InstantMessageListView.as_view(), name='instant-message-list'),
    path('new/', InstantMessageCreateView.as_view(), name='instant-message-create'),
]
