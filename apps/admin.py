from django.contrib import admin
from apps.models import Trener
@admin.register(Trener)
class TrenerAdmin(admin.ModelAdmin):
    pass

