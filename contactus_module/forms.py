from django import forms
from .models import ContactUs


class ContactModelForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        exclude = ['response', 'create_date', 'is_read_by_admin']
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'title': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'massage': forms.Textarea()
        }


class ProfileForm(forms.Form):
    user_image = forms.FileField()
