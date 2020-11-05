from django.urls import path, include

from .import views

urlpatterns = [
    path('', views.DoctorsList.as_view(), name='all-doctors'),
    path('<int:pk>/', views.DoctorDetail.as_view(), name='doctor-detail'),
    path('create/', views.DoctorCreate.as_view(), name='doctor-create'),
    path('update/<int:pk>/', views.DoctorsUpdate.as_view(), name='doctor-update'),
    path('delete/<int:pk>/', views.DeleteDoctor.as_view(), name='doctor-delete')

]