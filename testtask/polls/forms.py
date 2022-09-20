from django import forms


class UploadFileForm(forms.Form):
    file = forms.FileField(label='Выберете файл')
    
class AddressForm(forms.Form):
    address = forms.CharField(label='Введите адрес')
    radius = forms.IntegerField(label='Введите радиус (км)', min_value=1)