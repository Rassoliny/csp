from django import forms
from softwareapp.models import Category, Software, Transfer


class CategoryCreateForm(forms.ModelForm):
    class Meta:
       model = Category
       fields = ('name', 'license_type')

    def __init__(self, *args, **kwargs):
        super(CategoryCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class SofwareForm(forms.ModelForm):
    class Meta:
        model = Software
        fields = ('name', 'category', 'license_term', 'owner', 'license_key')

    def __init__(self, *args, **kwargs):
        super(SofwareForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class TransferCreateForm(forms.ModelForm):
    class Meta:
        model = Transfer
        fields = ('source', 'destination', 'software')

    def __init__(self, *args, **kwargs):
        super(TransferCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class SearchWarehouseForm(forms.Form):
    warehouse = forms.CharField(label='Введите имя компьютера')


