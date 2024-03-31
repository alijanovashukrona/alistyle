
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

from asosiy.views import LoginsizHome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/',include('userapp.urls')),
    path('buyurtma/',include('buyurtma.urls')),
    path('asosiy/',include('asosiy.urls')),
    path('',LoginsizHome.as_view())
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

