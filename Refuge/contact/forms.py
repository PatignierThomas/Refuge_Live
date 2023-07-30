from django import forms
from .models import ContactForm


class ContactFormForm(forms.ModelForm):
    # name = forms.CharField(max_length=100, required=True)
    # email = forms.EmailField(required=True, error_messages={"required": "Veuillez saisir une adresse mail"})
    # subject = forms.CharField(max_length=200, required=True, error_messages={"required": "Veuillez saisir un sujet"})
    # message = forms.CharField(required=True, error_messages={"required": "Veuillez saisir un message"})

    class Meta:
        model = ContactForm
        fields = ['name', 'email', 'message', 'subject']
