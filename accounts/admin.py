from django.contrib import admin
from .models import CustomUser
from import_export.admin import ImportExportModelAdmin

# Register your models here.


admin.site.register(CustomUser, ImportExportModelAdmin )
