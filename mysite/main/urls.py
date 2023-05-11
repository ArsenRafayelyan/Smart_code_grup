from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='reg'),
    path('welcome/',views.welcome, name='welcome'),
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('check/', views.check, name='check'),
    path(r'verify/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/',  views.activate, name='activate'),
]