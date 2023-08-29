from django.contrib import admin
from .models import club,player,tournament,member,match

# Register your models here.
admin.site.register(club)
admin.site.register(player)
admin.site.register(tournament)
admin.site.register(member)
admin.site.register(match)