from django.urls import path
from .views import SignUpView

app_name = 'registration'
urlpatterns = [
    path('', SignUpView.as_view(), name='register'),
]