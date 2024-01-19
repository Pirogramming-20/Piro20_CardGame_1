from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','score']



####소셜로그인 구분라인##############################################################

# from allauth.account.forms import SignupForm

# class CustomSignupForm(SignupForm):
#     user_id = forms.CharField(max_length=100)

#     def save(self, request):
#         user = super(CustomSignupForm, self).save(request)
#         user.user_id  = self.cleaned_data['user_id']
#         user.save()
#         return user