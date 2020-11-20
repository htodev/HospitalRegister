from django.urls import path
from .import views

urlpatterns = [
    path('', views.EnrollmentList.as_view(), name='all-enrollments'),
    path('<int:pk>/', views.EnrollmentDetail.as_view(), name='enrollment-detail'),
    path('create/', views.EnrollmentCreate.as_view(), name='enrollment-create'),
    path('update/<int:pk>/', views.EnrollmentUpdate.as_view(), name='enrollment-update'),
    path('delete/<int:pk>/', views.EnrollmentDelete.as_view(), name='enrollment-delete')
]
