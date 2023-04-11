
from django.urls import path
from .views import UploadFeed
from django.conf.urls.static import static

urlpatterns = [
    path('upload', UploadFeed.as_view())
]
