from django import forms
from warehouseapp.models import Warehouse


class WarehouseCreateForm(forms.ModelForm):
    class Meta:
       model = Warehouse
       fields = ('name', 'warehouse_type')

    def __init__(self, *args, **kwargs):
        super(WarehouseCreateForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

