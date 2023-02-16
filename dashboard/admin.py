from django.contrib import admin
from .models import Category, Caso, Score, Donate
# Models que aparecem na área administrativa


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...


@admin.register(Caso)
class CasoAdmin(admin.ModelAdmin):
    ...


@admin.register(Donate)
class DonateAdmin(admin.ModelAdmin):
    ...


@admin.register(Score)
class ScoreAdmin(admin.ModelAdmin):
    ...
