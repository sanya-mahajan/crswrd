from django.contrib import admin

# Register your models here.
from .models import Ques,Player


admin.site.register(Ques)
admin.site.register(Player)