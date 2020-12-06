from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('Smudge/', admin.site.urls),
    path('', include('common.urls')),
    path('auth/', include('doctors_auth.urls')),
    path('enrollments/', include('enrollment_system.urls')),
    path('hospital_units/', include('hospital_units.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

