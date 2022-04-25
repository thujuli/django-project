from django.forms import ModelForm
from django import forms
from .models import Book


class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        widgets = {
            'genres': forms.CheckboxSelectMultiple()
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['genres'].widget.attrs.update({'class': 'form-check'})
