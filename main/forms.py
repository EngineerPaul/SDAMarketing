from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Cost, CostGroup, Vacancy


# ADMIN FORMS

class CostForm(forms.ModelForm):
    title = forms.CharField(
        widget=CKEditorUploadingWidget(),
        label='Название услуги',
        max_length=350,
    )
    cost = forms.CharField(
        widget=CKEditorUploadingWidget(),
        label='Стоимость',
        max_length=200,
    )
    term = forms.CharField(
        widget=CKEditorUploadingWidget(),
        label='Срок',
        max_length=200,
        required=False,
    )

    class Meta:
        model = Cost
        fields = '__all__'


class CostGroupForm(forms.ModelForm):
    title = forms.CharField(
        widget=CKEditorUploadingWidget(),
        label='Название группы цен',
        max_length=255,
    )

    class Meta:
        model = CostGroup
        fields = '__all__'


class ProjectForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget(),
        label='Содержание',
    )


class VacancyForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Vacancy
        fields = '__all__'
