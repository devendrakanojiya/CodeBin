from django.contrib import admin
from django.urls import path,include
from codebin import views
urlpatterns = [
    path('',views.index,name='home'),
    path('find',views.find,name='find'),
    path('about',views.about,name='about'),
    path('privacy', views.privacy, name='privacy')

    # path('login',views.login_user,name='loginUser'),
    # path('logout',views.logout_user,name='logout')

]
