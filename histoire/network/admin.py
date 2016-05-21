from django.contrib import admin

# Register your models here.

from network.models import Profil
from articles.models import GeneralArticle, Character, People, Period, Region, Religion, Philosophy, Art, Battle, Invention, War, CharacterArticle, PeopleArticle, PeriodArticle, RegionArticle, ReligionArticle, PhilosophyArticle, ArtArticle, BattleArticle, InventionArticle, WarArticle

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    list_filter = ('author',)
    date_hierarchy = 'date'
    ordering = ('date',)
    search_fields = ('author','title','contents') #Comment avoir la categorie ???
    

admin.site.register(GeneralArticle, ArticleAdmin)
admin.site.register(CharacterArticle, ArticleAdmin)
admin.site.register(PeopleArticle, ArticleAdmin)
admin.site.register(RegionArticle, ArticleAdmin)
admin.site.register(PeriodArticle, ArticleAdmin)
admin.site.register(ReligionArticle, ArticleAdmin)
admin.site.register(PhilosophyArticle, ArticleAdmin)
admin.site.register(ArtArticle, ArticleAdmin)
admin.site.register(InventionArticle, ArticleAdmin)
admin.site.register(BattleArticle, ArticleAdmin)
admin.site.register(WarArticle, ArticleAdmin)
admin.site.register(Character)
admin.site.register(People)
admin.site.register(Period)
admin.site.register(Region)
admin.site.register(Religion)
admin.site.register(Philosophy)
admin.site.register(Art)
admin.site.register(Invention)
admin.site.register(Battle)
admin.site.register(War)
admin.site.register(Profil)
