from django.contrib import admin
from .models import CustomUser
from import_export.admin import ImportExportModelAdmin
from import_export.formats import base_formats
# Register your models here.


class CustomUserAdmin(ImportExportModelAdmin):
    formats = (
        base_formats.CSV,
        base_formats.XLS,
        base_formats.ODS,
        base_formats.JSON,
        base_formats.HTML,
    )


admin.site.register(CustomUser, CustomUserAdmin)

