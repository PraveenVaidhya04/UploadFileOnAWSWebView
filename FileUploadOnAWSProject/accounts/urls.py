from django.urls import path
from . import views
from django.contrib.auth import views as auth_login

urlpatterns = [
    path('registration/', views.AccountRegistrationView.as_view(), name="account_registration"),

    path('login/', auth_login.LoginView.as_view(template_name='accounts/login.html'), name="account_login"),

    path('logout/', auth_login.LogoutView.as_view(), name="account_logout"),

]