from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Cost, CostGroup, Vacancy


class FeedBackForm(forms.Form):
    name = forms.CharField(max_length=63, required=True)
    contact = forms.CharField(max_length=63, required=True)
    text = forms.CharField(required=True, widget=forms.Textarea())
    link = forms.CharField(max_length=127, required=True,
                           show_hidden_initial=True)


# ADMIN FORMS

class CostForm(forms.ModelForm):
    title = forms.CharField(
        widget=CKEditorUploadingWidget(),
        label='Название услуги',
        max_length=255,
    )
    cost = forms.CharField(
        widget=CKEditorUploadingWidget(),
        label='Стоимость',
        max_length=63,
    )
    term = forms.CharField(
        widget=CKEditorUploadingWidget(),
        label='Срок',
        max_length=31,
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
