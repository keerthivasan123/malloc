from django.db import models
# Create your models here.
class Mentor(models.Model):
    mentorname = models.CharField(max_length=264)
    mentorphoto = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    mentorgmailid = models.CharField(max_length=264)
    mentorphoneno = models.IntegerField()
    state = models.CharField(max_length=264)
    city = models.CharField(max_length=264)
    mentorspecialisation = models.CharField(max_length=264)


def __str__(self):
    return self.mentorname, self.mentorgmailid