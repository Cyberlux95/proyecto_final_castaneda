from django.db import models
from django.contrib.auth.models import User

# Create your models here.


# esta clase es del perfil del usuario
class Profile(models.Model):
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(blank=True)
    bio = models.CharField(default='Hola, Blogger', max_length=100)
    # image = models.ImageField(default='default.png')    #aun no incorporo la parte de imagenes

    def __str__(self):
        return f'Perfil de {self.username}' #{self.user.username}   #no se si es unicamente username o .user.username



#### seccion aun no testeada

# para follow y unfollow

#    def following(self):
        user_ids = Relationship.objects.filter(from_user=self.user)\
									.values_list('to_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)
    
#    def followers(self):
        user_ids = Relationship.objects.filter(to_user=self.user)\
									.values_list('from_user_id', flat=True)
        return User.objects.filter(id__in=user_ids)


#class Relationship(models.Model):
#	from_user = models.ForeignKey(User, related_name='relationships', on_delete=models.CASCADE)
#	to_user = models.ForeignKey(User, related_name='related_to', on_delete=models.CASCADE)

#	def __str__(self):
#		return f'{self.from_user} to {self.to_user}'
