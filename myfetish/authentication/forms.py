from captcha.widgets import ReCaptchaV3
from django import forms
from django.contrib.auth.forms import UserCreationForm
from captcha.fields import ReCaptchaField


from django.contrib.auth.models import User


class NewUserForm(UserCreationForm):
    # E-MAIL, USERNAME, pass (x2), captcha
    email = forms.EmailField(required=True)
    captcha = ReCaptchaField(widget=ReCaptchaV3, label='')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


