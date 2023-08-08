from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    bio = models.CharField(default='Hola, Blogger', max_length=100)
    # image = models.ImageField(default='default.png')

    def __str__(self):
        return f'Perfil de {self.username}' #{self.user.username}


