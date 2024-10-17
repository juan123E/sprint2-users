from django.urls import path, include
from usuarios.views import HomeView

urlpatterns = [
    path('',include('django.contrib.auth.urls'))
]
