from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name = 'login'
urlpatterns = [
    path('', LoginView.as_view(template_name='login/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page='login:login'), name='logout'),
]