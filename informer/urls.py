"""informer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('auth/', include('authentication.urls')),
    path('admin/', include('admins.urls')),
    path('client/', include('clients.urls')),
    path('core/', include('core.urls')),
    path('instant_message/', include('instant_messages.urls')),
    path('lesson/', include('lessons.urls')),
    path('project/', include('projects.urls')),
    path('timed_message/', include('timed_messages.urls')),
    path('message/', include('tmessages.urls')),

    path('adminka/', admin.site.urls),
]
