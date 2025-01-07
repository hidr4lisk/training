from django.contrib import admin
from django.urls import path, include
from .views import home  # Asegúrate de importar la vista home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', include('registration.urls')),
    path('login/', include('login.urls')),
    path('', home, name='home'),  # Agregar esta línea
]