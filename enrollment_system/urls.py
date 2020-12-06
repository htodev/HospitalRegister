from django.contrib.auth.decorators import login_required
from django.urls import path
from .import views

urlpatterns = [
    path('', login_required(views.EnrollmentList.as_view()), name='all-enrollments'),
    path('<int:pk>/', views.EnrollmentDetail.as_view(), name='enrollment-detail'),
    path('create/', login_required(views.EnrollmentCreate.as_view()), name='enrollment-create'),
    path('update/<int:pk>/', login_required(views.EnrollmentUpdate.as_view()), name='enrollment-update'),
    path('delete/<int:pk>/', login_required(views.EnrollmentDelete.as_view()), name='enrollment-delete')
]
