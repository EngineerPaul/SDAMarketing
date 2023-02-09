from django.contrib import admin

from .models import (
    Cost, CostGroup, Article, Direction, Industry, Vacancy, FeedBack
)
from .forms import (
    VacancyForm, CostForm, CostGroupForm, ArticleForm
)


class CostAdmin(admin.ModelAdmin):
    form = CostForm
    list_display = ('title', 'cost')
    list_display_links = ('title',)


class CostGroupAdmin(admin.ModelAdmin):
    form = CostGroupForm
    list_display = ('title', )
    list_display_links = ('title',)

    def title(self, obj):
        return obj.id


class ArticleAdmin(admin.ModelAdmin):
    form = ArticleForm
    prepopulated_fields = {"slug": ("title", ), }


class VacancyAdmin(admin.ModelAdmin):
    form = VacancyForm
    list_display = ('title',)
    list_display_links = ('title',)


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'answered', )
    list_display_links = ('name',)

    def title(self, obj):
        return obj.id


admin.site.register(Cost, CostAdmin)
admin.site.register(CostGroup, CostGroupAdmin)

admin.site.register(Article, ArticleAdmin)
admin.site.register(Direction)
admin.site.register(Industry)

admin.site.register(Vacancy, VacancyAdmin)

admin.site.register(FeedBack, FeedBackAdmin)
