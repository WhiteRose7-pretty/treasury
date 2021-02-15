from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('who-we-are/', views.about_us, name='about_us'),
    path('policy-notice/', views.policy_notice, name='policy_notice'),
    path('terms-of-service/', views.terms_service, name='terms_of_service'),
    path('fx-data_graph/', views.rates_data_graph, name='rates_data_graph'),
    path('workbench/', views.workbench, name='workbench'),
    path('workbench2/', views.workbench2, name='workbench2'),
  #  path('api_gateway/', views.api_gateway, name='api_gateway'),
    path('post_message/', views.post_message, name='post_message'),
    path('cron_test/', views.cron_test, name='cron_test'),
    path('connection_test/', views.connection_test, name='connection_test'),
]

