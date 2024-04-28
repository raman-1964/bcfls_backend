from rest_framework import serializers
from .models import Banner,User,NewsEvents,Opportunities,Gallery

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields="__all__"
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class NewsEventsSerializer(serializers.ModelSerializer):
    class Meta:
        model=NewsEvents
        fields="__all__"

class OpportunitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Opportunities
        fields="__all__"

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model=Gallery
        fields="__all__"
