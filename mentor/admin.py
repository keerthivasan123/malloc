from django.contrib import admin

from .models import Mentor

class MentorAdmin(admin.ModelAdmin):
  list_display = ('mentorname', 'mentorgmailid', 'approved', 'mentorphoneno', 'state', 'mentorspecialisation')
  list_display_links = ('mentorname',)
  list_filter = ('state','mentorspecialisation')
  list_editable = ('approved',)
  search_fields = ('mentorname', 'mentorgmailid', 'approved', 'mentorphoneno', 'state', 'mentorspecialisation')
  list_per_page = 6
admin.site.register(Mentor, MentorAdmin)