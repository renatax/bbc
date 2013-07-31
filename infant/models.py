from django.db import models
from django.contrib.auth.models import User, UserManager
import datetime


class Person(models.Model):
	GENDER_CHOICE = (('M', 'Male'), ('F', 'Female'),)
	gender = models.CharField(max_length=1, default='M')
	birthday = models.DateField(auto_now=True)
	user = models.OneToOneField(User)


class Action(models.Model):
	creator = models.ForeignKey(Person, related_name='+', null=True)
	receiver = models.ForeignKey(Person, related_name='+', null=True)

	class Meta:
		abstract = True

	def __unicode__(self):
		return str(self.pk)


class Item(models.Model):
	name = models.CharField(max_length=30)
	description = models.TextField(max_length=300)

	class Meta:
		abstract = True

	def __unicode__(self):
		return str(self.name)+': '+str(self.description)


class Toy(Item):
	toy_type = models.CharField(max_length=20)


class Food(Item):
	CHOICE = (('S', 'Solid Food'), ('L', 'Liquid Food'))
	UNITS = (('Oz', 'Ounce'), ('Jar', 'Jar'), ('Pc', 'Piece'))
	unit = models.CharField(max_length=20, choices=UNITS)
	food_type = models.CharField(max_length=20, choices=CHOICE)


class Feeding(Action):
	helper = models.ForeignKey(Person, related_name='helper', null=True)  # extra helper if any
	# help_type = models.OneToOneField(Person)
	time = models.DateTimeField(default=datetime.datetime.now)
	amount = models.DecimalField(max_digits=5, decimal_places=2)


class FeedingLiquids(Feeding):
	food = models.ForeignKey(Food, limit_choices_to={'food_type': 'L'})


class FeedingSolids(Feeding):
	food = models.ForeignKey(Food, limit_choices_to={'food_type': 'S'})


class Nap(Action):
	startAt = models.DateTimeField(default=datetime.datetime.now)
	endAt = models.DateTimeField(default=datetime.datetime.now)


class Diapering(Action):
	CHOICES = ((True, 'Yes'), (False, 'No'),)
	ointment = models.BooleanField(choices=CHOICES, default=False)
	bm = models.BooleanField(choices=CHOICES, default=False)
	wet = models.BooleanField(choices=CHOICES, default=False)


