from django.contrib import admin
from .models import Applications, AdvUser
from .models import Category
# Register your models here.


admin.site.register(Category)
admin.site.register(AdvUser)

@admin.register(Applications)
class ApplicationsAdmin(admin.ModelAdmin):
    list_display = ('title', 'deck', 'category', 'date_create', 'time_create', 'status')
    model = Applications
