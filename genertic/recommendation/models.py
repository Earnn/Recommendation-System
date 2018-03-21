 # -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea,TextInput,FileInput,ChoiceField,Select,BooleanField
from datetime import datetime
from django.contrib.postgres.fields import ArrayField

# Create your models here.

class NPArray(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	q_array = ArrayField(models.CharField(max_length=1000,default=[[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]]),blank=True,null=True
           
        )
 #    # Valid
	# NPArray(q_array=[
 #    [2, 3],
 #    [2, 1],
	# ])

    
	r_array = ArrayField(ArrayField(models.IntegerField(blank=True,null=True)),blank=True,null=True)
	# (r_array=[
 #    [2, 3],
 #    [2, 1],
	# ])

	created_at = models.DateTimeField(auto_now_add=True,null=True,)
	# r_array=[[0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.]]
	# q_array=[[0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.],
 #       [0., 0., 0., 0.]]
	def __str__(self):
		return "%s"%(self.q_array)
class Board(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	pieces = ArrayField(ArrayField(models.IntegerField()))

# Valid
Board(pieces=[[0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.],
       [0., 0., 0., 0.]])

# Not valid

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

class Qtable(models.Model):
	table = ArrayField(
        ArrayField(
            models.IntegerField(max_length=10, blank=True),
            size=8,
        ),
        size=8,
    )


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
	def __str__(self):
		return "%s"%(self.name)

class Menues(models.Model):
	
	store = models.ForeignKey(Store,on_delete=models.SET_NULL,blank=True,null=True)
	name = models.CharField(max_length=100)
	price = models.FloatField(null=True, blank=True, default=None)
	image=models.ImageField(upload_to='menu/',blank=True,null=True)
	isSell = models.BooleanField(default=True)
	created_at = models.DateTimeField(auto_now_add=True,null=True,)
	def __str__(self):
		return "%s"%(self.name)

class User_session(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	action = models.CharField(max_length=50,blank=True,null=True)
	value = models.CharField(max_length=100,blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True,null=True,)

class Order(models.Model):
	store = models.ForeignKey(Store,on_delete=models.SET_NULL,blank=True,null=True)
	menu = ArrayField(models.CharField(max_length=500), blank=True,null=True)
	amount = ArrayField(models.CharField(max_length=500), blank=True,null=True)
	user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	created_at = models.DateTimeField(auto_now_add=True,null=True,)
	def __str__(self):
		return "%s"%(self.menu)
	
class Informations(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True,null=True)
	age = models.IntegerField(default=0,blank=True,null=True)
	birthdate = models.DateField(blank=True,null=True)
	sex = models.CharField(max_length=10,blank=True,null=True)
	salary = models.CharField(max_length=50,blank=True,null=True)
	size = models.CharField(max_length=10,blank=True,null=True)
	breakfast = models.BooleanField(default=0)
	lunch = models.BooleanField(default=0)
	dinner = models.BooleanField(default=0)
	late = models.BooleanField(default=0)
	# taste = models.BooleanField(default=0)
	# price = models.BooleanField(default=0)
	# service = models.BooleanField(default=0)
	# clean = models.BooleanField(default=0)
	# at = models.BooleanField(default=0)
	# location = models.BooleanField(default=0)
	# facebook = models.BooleanField(default=0)
	# twitter = models.BooleanField(default=0)
	# instagram = models.BooleanField(default=0)
	# line = models.BooleanField(default=0)
	japanese = models.BooleanField(default=0)
	thai = models.BooleanField(default=0)
	diet = models.BooleanField(default=0)
	shabu = models.BooleanField(default=0)
	grill = models.BooleanField(default=0)
	steak = models.BooleanField(default=0)
	fastfood = models.BooleanField(default=0)
	cake = models.BooleanField(default=0)
	dessert = models.BooleanField(default=0)
	coffee = models.BooleanField(default=0)
	juice = models.BooleanField(default=0)
	created_at = models.DateTimeField(auto_now_add=True,null=True,)
	def __str__(self):
		return "%s"%(self.user)

