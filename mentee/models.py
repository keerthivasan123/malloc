from django.db import models
from mentor.models import Mentor

class startup_Details(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    startupname = models.CharField(max_length=200)
    websitelink = models.CharField(max_length=200)
    applink = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=264)
    zipcode = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    natureofthecompany = models.CharField(max_length=264)
    UdhyogAadhar = models.IntegerField()
    startlogo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    password = models.CharField(max_length=78,default='123')


    def __str__(self):
        return self.startupname

class team_member(models.Model):
    startup = models.ForeignKey(startup_Details, on_delete=models.CASCADE)
    membername = models.CharField(max_length=264,default='name')
    memberrole = models.CharField(max_length=264)
    memberphoto = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    descriptionmember = models.TextField(blank=True)
    linkedinurl = models.CharField(max_length=264)
    gmailid = models.CharField(max_length=264)

    def __str__(self):
        return self.membername

class project_details(models.Model):
    project_name = models.CharField(max_length=264)
    dev_type = models.CharField(max_length=264)
    app_type = models.CharField(max_length=264)
    project_des = models.CharField(max_length=600,default='abcd')
    def __str__(self):
        return self.project_name



