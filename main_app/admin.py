from django.contrib import admin
from .models import Whale # import the Artist model from models.py
# Register your models here.

admin.site.register(Whale) # this line will add the model to the admin panel
