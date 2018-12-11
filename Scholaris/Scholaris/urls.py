from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Result_Analysis.urls')),
    path('forum/',include('Discussion_Forum.urls')),
    path('test/', include('Test_Designing.urls')),
    path('api/', include('restScholaris.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
