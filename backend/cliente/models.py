from django.db import models

# Aqui se ponen los modelos para las tablas, por ahora no estan separados
class Direccion(models.Model):
    direccionId = models.AutoField(primary_key=True)
    pais = models.CharField(max_length=50, null=True, blank=True)
    ubicacion = models.CharField(max_length=50, null=True, blank=True)
    codigoPostal = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"{self.ubicacion}, {self.pais}"


class Tarjeta(models.Model):
    tarjetaID = models.AutoField(primary_key=True)
    numeroTarjeta = models.BigIntegerField()
    tipo = models.CharField(max_length=50, choices=[
        ('VISA', 'VISA'),
        ('MASTERCARD', 'MASTERCARD'),
        ('DINERS', 'DINERS')
    ])
    titular = models.CharField(max_length=50)
    CVV = models.IntegerField()

    def __str__(self):
        return f"{self.tipo} - {self.titular}"


class Cliente(models.Model):
    clienteId = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=50)
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    tarjeta = models.ForeignKey(Tarjeta, on_delete=models.CASCADE)
    direccion = models.ForeignKey(Direccion, on_delete=models.CASCADE)

    def __str__(self):
        return self.nickname