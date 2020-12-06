from django.urls import path

from .import views

urlpatterns = [
    path('register/', views.register_user, name="register user"),
    path('login/', views.login_user, name="login"),
    path('logout', views.logout_user, name="logout user"),
    path('profile/', views.doctor_profile_landing_page, name='doctor profile'),
    path('profile/edit/', views.doctor_profile_edit, name='doctor profile edit')
]
