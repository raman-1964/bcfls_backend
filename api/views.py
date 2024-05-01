from django.shortcuts import render
from rest_framework import viewsets
from .models import Banner,User,NewsEvents,Opportunities,Gallery
from .serializers import BannerSerializer,UserSerializer,NewsEventsSerializer,NewsLetterSerializer,OpportunitiesSerializer,GallerySerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from django.db import models


# Create your views here.
class BannerViewSet(APIView):
    def get(self, request):
        item = Banner.objects.all()
        serializer = BannerSerializer(item, context={'request':request} ,many=True)
        return Response({"status":"success","data":serializer.data})

class UserViewSet(APIView):
    def get(self, request):
        item = User.objects.all()
        serializer = UserSerializer(item)
        return Response({"status":"success","data":serializer.data})

class NewsEventsViewSet(APIView):
    def get(self, request):
        queryset = NewsEvents.objects.all()
        if 'is_home_page' in request.query_params:
            queryset = queryset.filter(is_home_page=request.query_params['is_home_page'])
        if 'id' in request.query_params:
            queryset = queryset.filter(id=request.query_params['id'])
        serializer = NewsEventsSerializer(queryset, context={'request': request}, many=True)
        return Response({"status": "success", "data": serializer.data})

class OpportunitiesViewSet(APIView):
    def post(self, request):
        serializer = OpportunitiesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})
        else :
            return Response({"status":"error","data":serializer.errors})
        
class GalleryViewSet(APIView):
    def get(self, request): 
        queryset = Gallery.objects.all()  
        is_home_page_value = request.query_params.get('is_home_page')
        if is_home_page_value is not None:
            is_home_page_bool = is_home_page_value.lower() == 'true'
            queryset = queryset.filter(is_home_page=is_home_page_bool)
        serializer = GallerySerializer(queryset, context={'request': request}, many=True)
        return Response({"status": "success", "data": serializer.data})

class NewsLetterViewSet(APIView):
    def post(self, request):
        serializer = NewsLetterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success","data":serializer.data})
        else :
            return Response({"status":"error","data":serializer.errors})
      