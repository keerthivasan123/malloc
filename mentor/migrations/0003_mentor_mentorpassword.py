# Generated by Django 2.1.3 on 2019-03-02 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentor', '0002_mentor_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='mentor',
            name='mentorpassword',
            field=models.CharField(default='000', max_length=50),
        ),
    ]
