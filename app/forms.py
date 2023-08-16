from django import forms


class TextAreaForm(forms.Form):
    textarea = forms.CharField(max_length=100, widget=forms.Textarea, label='textarea')
