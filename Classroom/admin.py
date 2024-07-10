from django.contrib import admin

from Classroom.models import Classes, Instructor, Student, Assigments

# Register your models here.
admin.site.register(Classes)
admin.site.register(Student)
admin.site.register(Instructor)
admin.site.register(Assigments)
