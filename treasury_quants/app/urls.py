from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('who-we-are/', views.about_us, name='about_us'),
    path('policy-notice/', views.policy_notice, name='policy_notice'),
    path('terms-of-service/', views.terms_service, name='terms_of_service'),
    path('fx-data-graph/', views.rates_data_graph, name='rates_data_graph'),
    path('workbench/', views.workbench, name='workbench'),
    path('post-message/', views.post_message, name='post_message'),
    path('server-down/', views.server_down, name='server_down'),
    path('test-connection/', views.test_connection, name='test_connection'),
]

