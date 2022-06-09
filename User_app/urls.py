from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('',views.user_list,name='user_list'),
    path('add_user',views.Add_User,name='add_user'),
    path('profile/<int:primarykey>',views.user_Profile,name='profile'),
    path('edit_user/<int:primarykey>',views.Edit_User,name='edit_user'),
    path('delete/<int:primarykey>',views.Delete_profile,name='delete_user'),

]