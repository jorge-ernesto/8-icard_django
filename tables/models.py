from django.db import models

# Create your models here.

class Table(models.Model):
    number = models.IntegerField(unique=True, verbose_name="Numero")

    def __str__(self):
        return str(self.number)

    class Meta:
        verbose_name = "Mesa"  # Manipular nombre en el panel
        verbose_name_plural = "Mesas"  # Manipular nombre en el panel
