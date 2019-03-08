from django.db import models
from django.contrib.postgres.fields import ArrayField
# Create your models here.
class Mentor(models.Model):
    mentorname = models.CharField(max_length=264)
    mentorphoto = models.ImageField(upload_to='photos/%Y/', blank=True)
    mentorpassword=models.CharField(max_length=50,default='000')
    mentorgmailid = models.CharField(max_length=264)
    mentorphoneno = models.IntegerField()
    state = models.CharField(max_length=264)
    city = models.CharField(max_length=264)
    mentorspecialisation =models.CharField(max_length=264)
    approved = models.BooleanField(default=False)
    rating = models.IntegerField(default="5")


    def __str__(self):
        return self.mentorname