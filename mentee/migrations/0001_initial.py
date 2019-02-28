# Generated by Django 2.1.3 on 2019-02-28 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mentor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='startup_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('startupname', models.CharField(max_length=200)),
                ('websitelink', models.CharField(max_length=200)),
                ('applink', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=264)),
                ('zipcode', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True)),
                ('natureofthecompany', models.CharField(max_length=264)),
                ('UdhyogAadhar', models.IntegerField()),
                ('startlogo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentor.Mentor')),
            ],
        ),
        migrations.CreateModel(
            name='team_member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('memebername', models.CharField(max_length=264)),
                ('memberrole', models.CharField(max_length=264)),
                ('memberphoto', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('descriptionmember', models.TextField(blank=True)),
                ('linkedinurl', models.CharField(max_length=264)),
                ('gmailid', models.CharField(max_length=264)),
                ('startup', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mentee.startup_Details')),
            ],
        ),
    ]