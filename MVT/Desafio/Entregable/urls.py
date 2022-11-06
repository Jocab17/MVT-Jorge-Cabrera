from django.urls import path
from Entregable.views import mostrar_familiares


urlpatterns = [
    path('familiares/', mostrar_familiares)
]
