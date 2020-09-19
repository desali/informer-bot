from django.urls import path

from clients.views import ClientListView

urlpatterns = [
    path('', ClientListView.as_view(), name='client-list')
]
