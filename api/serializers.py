from rest_framework import serializers
from .models import Banner,User,NewsEvents,Opportunities,Gallery

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Banner
        fields="__all__"

    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)
           
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields="__all__"

class NewsEventsSerializer(serializers.ModelSerializer):
    keynoteSpeaker = UserSerializer(many=True)
    programCoordinator = UserSerializer(many=True)
    chairPerson = UserSerializer(many=True)
    class Meta:
        model=NewsEvents
        fields="__all__"
    
    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)
    
class OpportunitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Opportunities
        fields="__all__"

class GallerySerializer(serializers.ModelSerializer):
    class Meta:
        model=Gallery
        fields="__all__"
    
    def get_photo_url(self, obj):
        request = self.context.get('request')
        photo_url = obj.fingerprint.url
        return request.build_absolute_uri(photo_url)
    
