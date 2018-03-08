from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Populations(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	chromosome1 = models.CharField(max_length=1,null=True, blank=True )
	store1 = models.CharField(max_length=100,null=True, blank=True )
	chromosome2 = models.CharField(max_length=1,null=True, blank=True )
	store2 = models.CharField(max_length=100,null=True, blank=True )
	chromosome3 = models.CharField(max_length=1,null=True, blank=True )
	store3 = models.CharField(max_length=100,null=True, blank=True )
	chromosome4 = models.CharField(max_length=1,null=True, blank=True )
	store4 = models.CharField(max_length=100,null=True, blank=True )
	chromosome5 = models.CharField(max_length=1,null=True, blank=True ) 
	chromosome6 = models.CharField(max_length=1 ,null=True, blank=True)
	chromosome7 = models.CharField(max_length=1 ,null=True, blank=True)
	chromosome8 = models.CharField(max_length=1 ,null=True, blank=True)
	chromosome9 = models.CharField(max_length=1 ,null=True, blank=True)
	chromosome10 = models.CharField(max_length=1,null=True, blank=True )


class Menues(models.Model):

	name = models.CharField(max_length=100)
	price = models.FloatField(null=True, blank=True, default=None)
	image=models.ImageField(upload_to='menu/',blank=True,null=True)
	isSell = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True,null=True,)
	def __str__(self):
		return "%s"%(self.name)


class Store(models.Model):
	# user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	name = models.CharField(max_length=300)
	place = models.CharField(max_length=200)
	price = models.CharField(max_length=200,null=True, blank=True)
	# image=models.ImageField(upload_to='stores/')
	# day_open = models.CharField(max_length=200,null=True, blank=True)
	# time_open = models.TimeField(null=True, blank=True)
	# time_close = models.TimeField(null=True, blank=True)
	# phone = models.CharField(max_length=500,blank=True,null=True)
	tags = models.CharField(max_length=500,blank=True,null=True)
	# qrcode = models.ImageField(upload_to='qrcodes/',blank=True,null=True)
	category = models.CharField(max_length=100,blank=True,null=True)
	# quote = models.CharField(max_length=1000,blank=True,null=True)
	# latitude=models.FloatField(default=14.073565,null=True, blank=True)
	# longtitude=models.FloatField(default=100.607963,null=True, blank=True)
	# social = models.CharField(max_length=100,blank=True,null=True)
	# likes = models.ManyToManyField(User, related_name="likes",blank=True,null=True)
	# delivery_boundary = models.CharField(max_length=1000,blank=True,null=True)
	# delivery_payment = models.FloatField(null=True, blank=True, default=None)
	created_at = models.DateTimeField(auto_now_add=True,null=True,)

