from django.urls import path
from . import views

app_name = 'account_cycle'

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('confirm-email-password-reset/', views.password_reset, name='password_reset'),
    path('password-reset-call-back/', views.password_reset_call_back, name='password_reset_call-back'),
    path('invalid-page-call/', views.invalid_page_call, name='invalid_page-call'),
    path('profile/', views.profile, name='profile'),
    path('account_api/', views.call_account_api, name='account_api'),
    path('create-account/', views.create_account, name='create_account'),
    path('account-activation-callback/', views.account_activation_callback, name="account_activation_callback")
]

