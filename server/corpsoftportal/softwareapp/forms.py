from django import forms
from softwareapp.models import Category, Software


class CategoryCreateForm(forms.ModelForm):
    class Meta:
       model = Category
       fields = ('name', 'license_type')

    def __init__(self, *args, **kwargs):
        super(CategoryCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class SofwareCreateForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ('name', 'category', 'license_term', 'owner','license_key')

    def __init__(self, *args, **kwargs):
        super(SofwareCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


