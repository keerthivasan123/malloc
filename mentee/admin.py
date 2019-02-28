from django.contrib import admin
from .models import startup_Details
from .models import team_member

# Register your models here.
admin.site.register(startup_Details)
admin.site.register(team_member)
