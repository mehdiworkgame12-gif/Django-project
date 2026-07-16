from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='نام', max_length=100)
    age = forms.IntegerField(label='سن')
    email = forms.EmailField(label='ایمیل')
    message = forms.CharField(label='پیام', widget=forms.Textarea)