from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Smudge/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('doctors/', include('doctors.urls')),
    path('enrollments/', include('enrollment_system.urls'))
]
