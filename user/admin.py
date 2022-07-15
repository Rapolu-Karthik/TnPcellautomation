from django.contrib import admin
from .models import Feedback, User, Student, Professor

# Register your models here.
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Professor)
admin.site.register(Feedback)