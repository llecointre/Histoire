from django.contrib import admin

# Register your models here.

from network.models import Profil
from articles.models import Article, Category, Character, People, Period, Region

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','author','date','category', 'subcategories')
    list_filter = ('author', 'category', 'subcategories',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('author','title','contents','category','subcategories')
    

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category)
admin.site.register(Character)
admin.site.register(People)
admin.site.register(Period)
admin.site.register(Region)
admin.site.register(Profil)
