from django.db import models
import datetime

class Action(models.Model):
  user = models.CharField(max_length=20)
  infant = models.CharField(max_length=20) 
  class Meta:
    abstract = True
  def __unicode__(self):
    return str(self.pk)
class Feeding(Action):
  helper = models.CharField(max_length=20,default=None)
  help_type = models.CharField(max_length=20,default=None)
  food_type = models.CharField(max_length=20)
  amount = models.DecimalField(max_digits=5, decimal_places=2)  
  time=models.DateTimeField(default=datetime.datetime.now)

class FeedingL(models.Model):
  helper=models.TextField()
  help_type =models.TextField()
  type=models.TextField()
  amount=models.TextField()
  time=models.DateTimeField(default=datetime.datetime.now)

class FeedingS(models.Model):
  user=models.TextField()
  helper=models.TextField()
  help_type =models.TextField()
  infant=models.TextField()
  type=models.TextField()
  amount=models.TextField()
  time=models.DateTimeField(default=datetime.datetime.now)

class Nap(Action):
  startAt=models.DateTimeField(default=datetime.datetime.now)
  endAt=models.DateTimeField(default=datetime.datetime.now)

class Diapering(Action):
  CHOICES = (
        (True, 'Yes'),
        (False, 'No'),
           )
  d_type=models.TextField()
  ointment=models.BooleanField(choices = CHOICES, default = False)
  time=models.DateTimeField(default=datetime.datetime.now)


# Create your models here.
