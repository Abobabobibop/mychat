# mychat/urls.py
from django.contrib import admin
from django.urls import path, include
from chat import views as chat_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', chat_views.register, name='register'),
    path('chat/', chat_views.chat, name='chat'),
    path('online-users/', chat_views.online_users_view, name='online_users'),
    path('accounts/', include('django.contrib.auth.urls')),  # Provides login/logout.
]
