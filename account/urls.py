from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    #url('login/', views.user_login, name='login'),
    url('login/', auth_views.LoginView.as_view(), name='login'),
    url('logout/', auth_views.LogoutView.as_view(), name='logout'),
    url('', views.dashboard, name='dashboard'),
]
