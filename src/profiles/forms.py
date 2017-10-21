from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import profile
from django import forms
class editInfo(ModelForm):
	class Meta:
		model=profile
		fields=(
			'name1',
			'f_name',
			'm_name',
			'address',
			'p_pno',
			's_pno',
		)