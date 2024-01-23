from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'image', 'email', 'website', 'comment']
        exclude = ['article']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'name': 'name',
            'placeholder': 'Name',
            'id': 'name'
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            'name': 'email',
            'placeholder': 'Email',
            'id': 'email'
        })
        self.fields['website'].widget.attrs.update({
            'class': 'form-control',
            'name': 'website',
            'placeholder': 'Website',
            'id': 'website'
        })
        self.fields['comment'].widget.attrs.update({
            'class': 'form-control w-100',
            'name': 'comment',
            'placeholder': 'Comment',
            'id': 'comment',
            'cols': 30,
            'rows': 9
        })

        self.fields['image'].widget.attrs.update({
            'class': 'form-control w-100',
            'name': 'image',
            'id': 'image'
        })














