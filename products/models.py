from django.db import models
from categories.models import Category

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='products')
    price = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=False)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,  # on_delete=models.SET_NULL, evitara que se elimine en CASCADA.
        null=True,                  # null=True, significa que la columna de la clave foránea en la base de datos puede contener valores nulos (es decir, que no apunta a ninguna instancia de Category).
        blank=True                  # blank=True, significa que en un formulario el campo puede dejarse en blanco (es decir, no se requiere seleccionar una categoría)
    )

    class Meta:
        verbose_name = 'Producto'  # Manipular nombre en el panel
        verbose_name_plural = 'Productos'  # Manipular nombre en el panel

    def __str__(self):
        return self.title
