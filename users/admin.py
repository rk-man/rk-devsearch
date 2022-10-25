from django.contrib import admin

# Register your models here.
from users.models import Profile, Skill

admin.site.register(Profile)
admin.site.register(Skill)
