from django.contrib import admin
from .models import Staf,Course,Event,News,Statistics,Banner,NewStudents
# Register your models here.

admin.site.register(Staf)
admin.site.register(Course)
admin.site.register(Event)
admin.site.register(News)
admin.site.register(Statistics)
admin.site.register(Banner)
@admin.register(NewStudents)
class NewStudentAdmin(admin.ModelAdmin):
    list_display = ['tel','course','teacher','name','surname','status']
    search_fields = ['tel']