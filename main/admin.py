from django.contrib import admin

from .models import (
    Cost, CostGroup, Project, Direction, Industry, Vacancy, FeedBack,
    Slider
)
from .forms import (
    VacancyForm, CostForm, CostGroupForm, ProjectForm
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


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectForm
    prepopulated_fields = {"slug": ("title", ), }


class VacancyAdmin(admin.ModelAdmin):
    form = VacancyForm
    list_display = ('title',)
    list_display_links = ('title',)


class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact', 'answered', )
    list_display_links = ('name',)
    ordering = ('answered', 'name')

    def title(self, obj):
        return obj.id


class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', )
    list_display_links = ('title', )


admin.site.register(Cost, CostAdmin)
admin.site.register(CostGroup, CostGroupAdmin)

admin.site.register(Project, ProjectAdmin)
admin.site.register(Direction)
admin.site.register(Industry)

admin.site.register(Vacancy, VacancyAdmin)

admin.site.register(FeedBack, FeedBackAdmin)

admin.site.register(Slider, SliderAdmin)
