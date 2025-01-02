from django.contrib import admin
from django.urls import path, include
from core.views import home

urlpatterns = [
    path('', home, name='home'),  # Añade esta línea para la página principal
    path('admin/', admin.site.urls),
    path('auth/', include('authentication.urls')),
]