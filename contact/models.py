from django.db import models

# Create your models here. 
# Note that I have used an uppercase letter for class name

class Contact(models.Model):
  name = models.CharField(max_length=122)
  email = models.CharField(max_length=120)
  desc = models.TextField()
  date = models.DateField()
  # code to show name of the person who sent you the message
  def _str_(self):
    return self.name