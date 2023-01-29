from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User, Company, Employee, Resume

# @admin.register(User)
# class UserAdmin(UserAdmin):
#     fieldsets = (
#         *UserAdmin.fieldsets, # unpacks the existing useradmin fields
#         ('Additional Info', {'fields': ('about')})
#     )

# To add the custom fields to existing sections in a useradmin fieldsets
# fields = list(UserAdmin.fieldsets)
# fields[1] = ('Personal Info', {'fields': ('first_name', 'last_name', 'email', 'about')})
# UserAdmin.fieldsets = tuple(fields)
# admin.site.register(User, UserAdmin)

admin.site.register(Company)
admin.site.register(User)
admin.site.register(Employee)
admin.site.register(Resume)