from django.urls import path, include

from . import views

urlpatterns = [
    path('profile/', views.redirect_to_user_profile, name='user-redirect'),
    path('profile/<int:pk>/', views.UserProfileDetail.as_view(), name='user-detail'),
    path('', include('django.contrib.auth.urls')),
    path('register/', views.SignUp.as_view(), name='register')
]

