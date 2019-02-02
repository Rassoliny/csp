from django.contrib import admin
from .models import Software, Category, LicenseType, LicenseTerm, Transfer
# Register your models here.

admin.site.register(Software)
admin.site.register(Category)
admin.site.register(LicenseType)
admin.site.register(LicenseTerm)
admin.site.register(Transfer)