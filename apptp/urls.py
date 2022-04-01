from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index' ),
]

if settings.DEBUG:
from django.conf.urls.static import static
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)