from django.contrib import admin
from api.models import Company, Employee
# Register your models here.
class companyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'types', 'about')
    list_filter = ('name',)

class employeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'position')

admin.site.register(Company, companyAdmin)
admin.site.register(Employee, employeeAdmin)
