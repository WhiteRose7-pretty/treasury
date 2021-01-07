from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='home'),
    path('who-we-are/', views.about_us, name='about_us'),
    path('profile/', views.profile, name='profile'),
    path('policy-notice/', views.policy_notice, name='policy_notice'),
    path('terms-of-service/', views.terms_service, name='terms_of_service'),
]

