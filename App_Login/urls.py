from django import views
from django.urls import URLPattern, path
from App_Login import views
app_name='App_Login'

urlpatterns = [
    path('signup/',views.sign_up,name='sign_up'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
]