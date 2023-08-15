from django import forms


class TextAreaForm(forms.Form):
    text_area_field = forms.CharField(widget=forms.Textarea, label='textarea')
