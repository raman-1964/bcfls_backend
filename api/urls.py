from django.urls import path
from django.contrib import admin
from .views import BannerViewSet,UserViewSet,NewsEventsViewSet,OpportunitiesViewSet,NewsLetterViewSet,GalleryViewSet

admin.site.site_header = "IRFPS Admin"
admin.site.site_title = "IRFPS Admin Portal"
admin.site.index_title = "Welcome to India Research For Policy Studies Portal"

urlpatterns = [
    path('user/', UserViewSet.as_view()),
    path('banner/', BannerViewSet.as_view()),
    path('news-event/', NewsEventsViewSet.as_view()),
    path('opportunities/', OpportunitiesViewSet.as_view()),
    path('gallery/', GalleryViewSet.as_view()),
    path('news-letter/', NewsLetterViewSet.as_view())
]
