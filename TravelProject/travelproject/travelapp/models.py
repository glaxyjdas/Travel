from django.db import models

# Create your models here.
class Place(models.Model):
    name1=models.CharField(max_length=250)
    img1=models.ImageField(upload_to='pics')
    desc1=models.TextField()

    def __str__(self):
        return self.name1

class Team(models.Model):
    name2=models.CharField(max_length=250)
    img2=models.ImageField(upload_to='pics')
    desc2=models.TextField()

    def __str__(self):
        return self.name2