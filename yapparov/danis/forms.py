from django import forms

class PublishForm(forms.Form):
    header = forms.CharField(label='Header', widget=forms.TextInput(attrs={'class': 'form--title'}))
    content = forms.CharField(label='Content', widget=forms.Textarea(attrs={'class': 'form--content'}))
    is_publish = forms.BooleanField(label='Publish', required=False)
    date = forms.DateField()