from django.urls import path
from . import views

# from .views import CustomSignupView
app_name = "users"

urlpatterns = [
    path("", views.main, name="main"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("after_login/", views.after_login, name="afterlogin"),
    path('login/naver_login/callback/', views.naver_login_callback),
]