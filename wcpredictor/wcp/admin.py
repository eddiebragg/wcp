from django.contrib import admin
from wcpredictor.wcp import models


class GroupTeamInline(admin.TabularInline):
    model = models.GroupTeam


class GroupAdmin(admin.ModelAdmin):
    model = models.Group
    inlines = [
        GroupTeamInline,
    ]


admin.site.register(models.Game)
admin.site.register(models.Group, GroupAdmin)
admin.site.register(models.Team)
admin.site.register(models.Tournament)
admin.site.register(models.UserProfile)
