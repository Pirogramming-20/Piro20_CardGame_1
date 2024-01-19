from django.urls import path
from . import views

# from .views import CustomSignupView
app_name = "users"

urlpatterns = [
    path("", views.main, name="main"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("signup/", views.signup, name="signup"),
####소셜로그인 구분라인##############################################################
    # path('accounts/google/login/', CustomSignupView.as_view(), name='account_signup'),
]


