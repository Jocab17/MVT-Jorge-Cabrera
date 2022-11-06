from django.shortcuts import render
from Entregable.models import Familiares

# Create your views here.
def mostrar_familiares(request):

    f1 = Familiares(nombre = 'Deyi', apellido = 'Ferrer', edad = 61, parentesco = 'mamá', cumpleanios = '1961-08-05')
    f2 = Familiares(nombre = 'Deivis', apellido = 'Ferrer', edad = 29, parentesco = 'primo', cumpleanios = '1993-11-09')
    f3 = Familiares(nombre = 'Isabel', apellido = 'Ferrer', edad = 85, parentesco = 'abuela', cumpleanios = '1938-06-02')

    return render(request, 'Entregable/Templates/familiares.html', {'familiares': [f1, f2, f3]})