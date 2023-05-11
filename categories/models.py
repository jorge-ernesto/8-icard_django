from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories')

    class Meta:
        verbose_name = 'Categoría'  # Manipular nombre en el panel
        verbose_name_plural = 'Categorías'  # Manipular nombre en el panel

    def __str__(self):
        return self.title
