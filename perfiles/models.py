from django.db import models

# Create your models here.
class Profile(models.Model):
    username = 
    email =
    bio = models.CharField(default='Hola, Blogger', max_length=100)
    image =



class Post(model.Model):
    pass


#register va en views