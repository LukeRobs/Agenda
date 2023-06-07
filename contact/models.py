from django.db import models
from django.contrib.auth import get_user_model

class contact(models.Model):

    cargo = (
        ('administrativo', 'administrativo'),
        ('estagiario', 'estagiario'),
        ('defensor', 'defensor')
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    city = models.CharField(max_length=200)
    office = models.CharField(
        max_length=14,
        choices = cargo,
    )
    phone = models.CharField(max_length=11)
    email = models.EmailField(max_length=254)
    description = models.TextField(blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'