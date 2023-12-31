from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/auth/', include('djoser.urls')),
    path('api/v1/auth/', include('djoser.urls.jwt')),
    path('api/v1/accounts/', include('apps.accounts.urls')),
    path('api/v1/', include('apps.store.urls')),
    path('api/v1/', include('apps.content.urls')),

    path("__debug__/", include("debug_toolbar.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header  =  "Uncover Skincare Admin"
admin.site.site_title  =  "Uncover Skincare Admin site"
admin.site.index_title  =  "Uncover Skincare Admin"