from django.contrib import admin
from .models import *

model_list = [Sport, Natjecanje, Tim, RezultatUtakmice]

admin.site.register(model_list)