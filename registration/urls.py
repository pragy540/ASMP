from django.contrib import admin
from django.urls.conf import include
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    # path('login', views.login1, name="login"),
    # path('profile', views.profile, name="profile"),
    # path('register/', views.register, name='register'),
    # path('otp/', views.otp, name="otp"),
    # path('fav/<int:id>/', views.favourite_add, name="favourite_add"),
    # path('favourites', views.favourite_list, name="favourite_list"),
    # path('update', views.update, name='update'),
    # path('test', views.test, name="test"),
    # path('logout', views.logout_view, name="logout"),
    # path('personal_info_add', views.personal_info_add, name="personal_info_add"),
    # path('csv_profile', views.csv_profile, name="csv_profile"),
    # path('csv_users', views.csv_users, name="csv_users"),
    # path('csv_mentor', views.csv_mentor, name="csv_mentor"),

]
