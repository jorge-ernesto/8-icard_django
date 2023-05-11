from django.db import models

# Create your models here.

StatusEnum = {  # En tuplas, usar comilla doble, en lugar de comilla simple, esto para que se muestre en "Administración de Django" estas opciones ordenadas, parece que Python maneja de forma diferente las comillas dobles de las simples
    ("PENDING", "pending"),
    ("DELIVERED", "delivered")
}

class Order(models.Model):
    table = models.ForeignKey(
        'tables.Table',
        on_delete=models.SET_NULL,  # on_delete=models.SET_NULL, evitara que se elimine en CASCADA.
        null=True,                  # null=True, significa que la columna de la clave foránea en la base de datos puede contener valores nulos (es decir, que no apunta a ninguna instancia de Table).
        blank=True                  # blank=True, significa que en un formulario el campo puede dejarse en blanco (es decir, no se requiere seleccionar una categoría)
    )
    product = models.ForeignKey(
        'products.Product',
        on_delete=models.SET_NULL,  # on_delete=models.SET_NULL, evitara que se elimine en CASCADA.
        null=True,                  # null=True, significa que la columna de la clave foránea en la base de datos puede contener valores nulos (es decir, que no apunta a ninguna instancia de Product).
        blank=True                  # blank=True, significa que en un formulario el campo puede dejarse en blanco (es decir, no se requiere seleccionar una categoría)
    )
    status = models.CharField(max_length=255, choices=StatusEnum)
    created_at = models.DateTimeField(auto_now_add=True)
    close= models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Pedido'  # Manipular nombre en el panel
        verbose_name_plural = 'Pedidos'  # Manipular nombre en el panel

    def __str__(self):
        return str(self.table)
