
from django.urls import path
from .views import UploadFeed,Profile
from django.conf.urls.static import static

urlpatterns = [
    path('upload', UploadFeed.as_view()),
    path('profile', Profile.as_view())
]
