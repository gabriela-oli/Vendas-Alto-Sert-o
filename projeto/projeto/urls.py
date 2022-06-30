from django.conf import settings
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('site/', include('app.urls')),
    path('produto/', include('produto.urls')),
    path('empresa/', include('empresa.urls')),
    
]

# if settings.DEBUG:
#     urlpatterns = [
#         url(r'^media/(?P<path>.*))$',
#         serve, {'document_root':
#         settings.MEDIA_ROOT, }),]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
