from django.db import models

# Create your models here.
class profile(models.Model):
	name1  = models.CharField(max_length=50)
	f_name = models.CharField(max_length=50 , default='')
	m_name = models.CharField(max_length=50 , default='')
	dob    = models.CharField(max_length=50 , default='')
	address= models.CharField(max_length=50 , default='')
	p_pno  = models.CharField(max_length=20 , default='')
	s_pno  = models.CharField(max_length=20 , default='')
	#description = models.TextField(default='desc def text')

	def __str__(self):
		return self.name1
