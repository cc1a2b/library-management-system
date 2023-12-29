from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Genders, Roles, Users, Depositories, Semesters, Cities, Libraries, CustomUser


admin.site.register(Genders)
admin.site.register(Roles)
admin.site.register(Users)
admin.site.register(Depositories)
admin.site.register(Semesters)
admin.site.register(Cities)
admin.site.register(Libraries)
