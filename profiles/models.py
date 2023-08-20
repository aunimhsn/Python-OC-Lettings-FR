from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    class Meta:
        db_table = 'profiles_profile'
    
    user = models.OneToOneField(User, related_name='profiles_profile', on_delete=models.CASCADE)
    favorite_city = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.user.username
