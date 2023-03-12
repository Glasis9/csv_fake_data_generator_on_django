from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from schemas.models import User, DataSchemas

admin.site.register(User, UserAdmin)
admin.site.register(DataSchemas)
