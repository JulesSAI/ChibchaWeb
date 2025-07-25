from django.shortcuts import render, redirect
from .models import Cliente, Direccion, Tarjeta
# Create your views here.

def registrar_cliente(request):
    if request.method == 'POST':
        nickname = request.POST.get('nickname')
        email = request.POST.get('email')
        nombre = request.POST.get('nombre')
        telefono = request.POST.get('telefono')

        # Para simplificar, creamos dirección y tarjeta dummy
        direccion = Direccion.objects.create(pais="Colombia", ubicacion="Calle falsa 123", codigoPostal="0000")
        tarjeta = Tarjeta.objects.create(numeroTarjeta=1234567890123456, tipo='VISA', titular=nombre, CVV=123)

        Cliente.objects.create(
            nickname=nickname,
            email=email,
            nombre=nombre,
            telefono=telefono,
            direccion=direccion,
            tarjeta=tarjeta
        )

        return redirect('registrar_cliente')  # Redirige a la misma página

    return render(request, 'registrar_cliente.html')