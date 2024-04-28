from django.urls import path
from .views import BannerViewSet,UserViewSet,NewsEventsViewSet,OpportunitiesViewSet,GalleryViewSet

urlpatterns = [
    path('user/', UserViewSet.as_view()),
    path('banner/', BannerViewSet.as_view()),
    path('news-event/', NewsEventsViewSet.as_view()),
    path('opportunities/', OpportunitiesViewSet.as_view()),
    path('gallery/', GalleryViewSet.as_view())
]
