from django.contrib import admin
from .models import MembersModels, AlertModel
# Register your models here.

admin.site.register(MembersModels)
admin.site.register(AlertModel)