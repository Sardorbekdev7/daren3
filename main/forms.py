from django import forms
from main.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'name': 'name',
            'placeholder': 'Enter your name',
            'id': 'name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'name': 'email',
            'placeholder': 'Enter your email address',
            'id': 'email'
        })
        self.fields['subject'].widget.attrs.update({
            'class': 'form-control',
            'name': 'subject',
            'placeholder': 'Enter your subject',
            'id': 'subject'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control w-100',
            'name': 'message',
            'placeholder': 'Enter your message',
            'id': 'message',
            'cols': 30,
            'rows': 9
        })






