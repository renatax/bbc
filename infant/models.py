from django.db import models
import datetime



class Action(models.Model):
  user = models.CharField(max_length=20)
  infant = models.CharField(max_length=20) 
  class Meta:
    abstract = True
  def __unicode__(self):
    return str(self.pk)

class Food(models.Model):
    CHOICE = (('S','Solid Food'),('L', 'Liquid Food'))
    UNITS = (('Oz','Ounce'),('Jar','Jar'),('Pc','Piece'))
    name = models.CharField(max_length=30)
    unit = models.CharField(max_length=20,choices=UNITS)
    food_type = models.CharField(max_length=20, choices = CHOICE)

class Feeding(Action):
  helper = models.CharField(max_length=20,default=None)
  help_type = models.CharField(max_length=20,default=None)
  time=models.DateTimeField(default=datetime.datetime.now)
  amount = models.DecimalField(max_digits=5, decimal_places=2)  


class FeedingLiquids(Feeding):
  food = models.ForeignKey(Food,limit_choices_to={'food_type':'L'})

class FeedingSolids(Feeding):
  food = models.ForeignKey(Food,limit_choices_to={'food_type':'S'})
  
class Nap(Action):
  startAt=models.DateTimeField(default=datetime.datetime.now)
  endAt=models.DateTimeField(default=datetime.datetime.now)
class Diapering(Action):
  CHOICES = (
        (True, 'Yes'),
        (False, 'No'),
           )
  ointment=models.BooleanField(choices = CHOICES, default = False)
  bm =models.BooleanField(choices = CHOICES, default = False) 
  wet = models.BooleanField(choices = CHOICES, default = False)


# Create your models here.
