from django.contrib import admin
from organization.models import Organization, Employee, GroupRights, Employment

# Register your models here.
admin.site.register(Organization)
admin.site.register(Employee)
admin.site.register(GroupRights)
admin.site.register(Employment)
