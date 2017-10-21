from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
	f_name=models.CharField(max_length=20,null=True)
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	phone_no = models.CharField(max_length=12,default="+91")
	secondary_no = models.CharField(max_length=12,default="+91")
	address = models.TextField(default="")
	m_name=models.CharField(max_length=20,null=True)
	dob=models.CharField(max_length=20,null=True)
	def __str__(self):
		return self.user.username

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    Profile.objects.get_or_create(user=instance)
    instance.profile.save()