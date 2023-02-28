from django.contrib import admin
from .models import Category, Caso, Score, Donate
from django.views.decorators.csrf import csrf_exempt

# Models que aparecem na área administrativa


@csrf_exempt
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@csrf_exempt
@admin.register(Caso)
class CasoAdmin(admin.ModelAdmin):
    ...


@csrf_exempt
@admin.register(Donate)
class DonateAdmin(admin.ModelAdmin):
    ...


@csrf_exempt
@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    ...
