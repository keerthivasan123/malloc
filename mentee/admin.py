from django.contrib import admin
from .models import startup_Details
from .models import team_member

# Register your models here.
class MenteeAdmin(admin.ModelAdmin):
  list_display = ( 'startupname', 'state', 'city', 'natureofthecompany','mentor')
  list_display_links = ('startupname','mentor',)
  list_filter = ('startupname','state','city','mentor')
  search_fields = ('startupname', 'state', 'city', 'natureofthecompany', 'Udhyogaadhar')
  list_per_page = 6
admin.site.register(startup_Details,MenteeAdmin)
class team_member_Admin(admin.ModelAdmin):
  list_display = ( 'startup','membername', 'memberrole','linkedinurl')
  list_display_links = ('startup',)
  list_filter = ('startup',)
  search_fields = ('startupname', 'memberrole')
  list_per_page = 6
admin.site.register(team_member,team_member_Admin)