from django.contrib import admin

from .models import *
from .resources import VoterResource

from import_export.admin import ImportExportModelAdmin
# Register your models here.
class VoterAdmin(ImportExportModelAdmin):
    resource_classes = [VoterResource]
    list_display = ['admin', 'phone', 'otp', 'verified', 'voted', 'otp_sent']
    list_display_links = ['phone', 'admin']

class PositionAdmin(admin.ModelAdmin):
    list_display = ['name', 'max_vote', 'priority',]

class CandidateAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'photo', 'position',]

class VotesAdmin(admin.ModelAdmin):
    list_display = ['voter', 'position', 'candidate',]

admin.site.register(Voter, VoterAdmin)
admin.site.register(Votes, VotesAdmin)
admin.site.register(Position, PositionAdmin)
admin.site.register(Candidate, CandidateAdmin)