from django.urls import path
from .views import *

app_name="users"

urlpatterns=[
    path('login/', login),
    path('login/naver_login/callback/', naver_login_callback),
    #path('logout/', logout),
    #path('signup/', signup),
]