from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'phone', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your name', 'required': True}),
            'email': forms.EmailInput(attrs={'placeholder': 'example@mail.com', 'required': True}),
            'phone': forms.TextInput(attrs={'placeholder': 'Phone (optional)'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject (optional)'}),
            'message': forms.Textarea(attrs={'placeholder': 'Your message...', 'rows': 6, 'required': True}),
        }
