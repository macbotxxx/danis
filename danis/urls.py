from django.contrib import admin
from django.urls import path, include


from django.conf.urls.static import static
from danis import settings


urlpatterns = [
    path('admin/', admin.site.urls, name=admin),
    path('', include('accounts.urls')),
    path('accounts/', include('allauth.urls')),
]


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
