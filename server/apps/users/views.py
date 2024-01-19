from django.shortcuts import render, redirect
from apps.users.forms import SignupForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from .models import User,SocialUser
import json

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

def after_login(request):
    if request.method == 'POST':
        return redirect('users:afterlogin')


def socaial_signup(name, nickname):
    try:
        password = make_password(name)
        User.objects.create( password = password, nickname = nickname, score = 0)
        
        #accountpk = User.objects.get(user_id = name)
        #SocialUser.objects.create(name, nickname, accountpk)
    except:
        print("소셜 회원가입 error!!")
        return 0
    else: 
        print("소셜 화원가입 성공")
        return 1



def login(request):
    if request.method == "GET":
        form = AuthenticationForm()
        context = {
            'form': form,
        }
        return render(request, template_name='users/login.html', context=context)
    
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
        
    if request.method == "PUT":
        try:
            data = json.loads(request.body.decode('utf-8'))
            name = str(data.get('name'))
            nickname = str(data.get('nickname'))
            print("social user 데이터 수신 완료!")
        except:
            print("error!")
        else:
            try:
                s_user = User.objects.get(nickname = nickname)
            except:
                print("해당하는 s_user 없음!")
                socaial_signup(name, nickname) # 신규 로그인일 경우, 회원가입
                auth.login(request, s_user)   # 회원가입한 계정으로 로그인
                return redirect('users:main') 
                
            else: # 기존에 있는 회원 아이디일 경우
                print("s_user 찾음!")
                auth.login(request, s_user)  # 해당 값으로 로그인 
                return redirect('users:main')
                # 로그 아웃 버튼을 누를 때, 네이버 로그아웃, User 로그 아웃 둘다 수행 해야함

                          

def logout(request):
    auth.logout(request)
    return redirect('users:main')

  
  
def naver_login_callback(request):
    return render(request, 'users/naver_callback.html')   


