from django.contrib import admin
from django.urls import path
from core import views
from Portfolio.views import portfolio
from django.conf import settings

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('portfolio/', portfolio, name='portfolio'),
    path('contact/', views.contact, name='contact'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)