from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas principales
    path('', include('blog.urls')), 
    
    path('pages/', include('pages.urls')),
    
    path('accounts/', include('accounts.urls')),
    
    # App Messaging (mensajería entre usuarios)
    path('messages/', include('messaging.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
