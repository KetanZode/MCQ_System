from exam import models
from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from exam.models import que

# Register your models here.
class queAdmin(ModelAdmin):
    list_display = ["qno","ans"]
    search_fields = ["qno","que"]

admin.site.register(que,queAdmin)