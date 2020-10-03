from django.contrib import admin
from django.urls import path, include 
from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls.i18n import i18n_patterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')), 
   	
   	path('I18n/', include('django.conf.urls.i18n')), 
]

urlpatterns += i18n_patterns(
	path('', include('MainApp.urls')),
	path('auth/', include('AuthApp.urls')),
)

if settings.DEBUG:
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
