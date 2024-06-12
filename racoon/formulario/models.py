from django.db import models

# Create your models here.
#aqui creamos la bd de los productos 
class Marca(models.Model):
    nombre= models.CharField(max_length=50)

    def _str_(self):
        return self.nombre
    
class Producto(models.Model):
    nombre= models.CharField(max_length=50)
    precio=models.IntegerField()
    decripcion=models.TextField()
    marca=models.ForeignKey(Marca, on_delete=models.PROTECT)

    def _str_(self):
        return self.nombre
    

    #luego colocamos el siguiente comando en la cmd python manage.py makemigrations
    #y python manage.py migrate