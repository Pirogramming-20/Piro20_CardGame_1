
####소셜로그인 구분라인##############################################################

from allauth.account.adapter import DefaultAccountAdapter

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        user = super(CustomAccountAdapter, self).save_user(request, user, form, False)
        user.additional_info = form.cleaned_data.get('additional_info')
        if commit:
            user.save()
        return user