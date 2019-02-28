from django.db import models
# Create your models here.
class Mentor(models.Model):
    mentorname = models.CharField(max_length=264)
    mentorphoto = models.ImageField(upload_to='photos/%Y/', blank=True)
    mentorgmailid = models.CharField(max_length=264)
    mentorphoneno = models.IntegerField()
    state = models.CharField(max_length=264)
    city = models.CharField(max_length=264)
    hours_of_working = models.IntegerField(max_length=10, default="", editable=True)
    mentorspecialisation = models.CharField(max_length=264)


def __str__(self):
    return self.mentorname