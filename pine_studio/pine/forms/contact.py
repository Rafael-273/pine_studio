from django import forms
from ..models import DownloadEmail, Pack


class DownloadEmailForm(forms.ModelForm):
    class Meta:
        model = DownloadEmail
        fields = ['name', 'email', 'found_us_through', 'pack', 'consent_for_marketing']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full text-gray-800 px-4 py-2 rounded-md focus:outline-none',
                'placeholder': 'Digite seu nome'}),
            'email': forms.EmailInput(attrs={
                'class': 'w-full text-gray-800 px-4 py-2 rounded-md focus:outline-none',
                'placeholder': 'Digite seu e-mail'}),
            'found_us_through': forms.Select(attrs={
                'class': 'w-full text-black px-4 py-2 rounded-md focus:outline-none'}),
            'consent_for_marketing': forms.CheckboxInput(attrs={
                'class': 'form-check-input text-blue-600 border-gray-300 rounded cursor-pointer'}),
        }
    
    def __init__(self, *args, **kwargs):
        pack = kwargs.pop('pack', None)
        super().__init__(*args, **kwargs)

        if pack:
            self.fields['pack'].initial = pack
            self.fields['pack'].queryset = Pack.objects.filter(id=pack.id)