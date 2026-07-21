from django import forms
from captcha.fields import CaptchaField
class NameForm(forms.Form):
    name = forms.CharField(label='نام', max_length=100)
    age = forms.IntegerField(label='سن')
    email = forms.EmailField(label='ایمیل')
    message = forms.CharField(label='پیام', widget=forms.Textarea)
    captcha = CaptchaField()

    from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'message']

