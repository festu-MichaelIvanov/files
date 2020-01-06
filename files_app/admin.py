from django.contrib import admin

from files_app.models import FileInstance


@admin.register(FileInstance)
class FileInstanceAdmin(admin.ModelAdmin):
    pass
