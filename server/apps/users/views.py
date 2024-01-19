from django.shortcuts import render, redirect
from apps.users.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth

def main(request):
    return render(request, "users/main.html")


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('users:main')
        else:
            ctx={
                'form':form,
            }
            return render(request, 'users/signup.html',context=ctx) # 이부분 수정
    else:
        form = SignupForm()
        context={
            'form': form,
        }
        return render(request, template_name='users/signup.html', context=context)


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('users:main')
        else:
            context = {
                'form': form,
            }
            return render(request, template_name='users/login.html', context=context)
    else:
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, template_name='users/login.html', context=context)


def logout(request):
    auth.logout(request)
    return redirect('users:main')



####소셜로그인 구분라인##############################################################
# from allauth.socialaccount.views import SignupView

# class CustomSignupView(SignupView):

#     def get_context_data(self, **kwargs):
#         context = super(CustomSignupView, self).get_context_data(**kwargs)
#         # 컨텍스트에 필요한 추가 데이터를 포함시킵니다
#         return context

#     def form_valid(self, form):
#         # 폼이 유효할 때의 처리 로직을 커스터마이즈합니다
#         return super(CustomSignupView, self).form_valid(form)