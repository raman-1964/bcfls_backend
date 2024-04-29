from django.shortcuts import render
from rest_framework import viewsets
from .models import Banner,User,NewsEvents,Opportunities,Gallery
from .serializers import BannerSerializer,UserSerializer,NewsEventsSerializer,OpportunitiesSerializer,GallerySerializer
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
    def get(self, request, id=None):
        if id :
            item = NewsEvents.objects.get(id=id)
            serializer = NewsEventsSerializer(item, context={'request':request} ,many=True)
            return Response({"status":"success","data":serializer.data})
        else :
            if 'is_home_page' in request.query_params:
                if request.query_params['is_home_page'].lower() == 'true':
                    try:
                        item = NewsEvents.objects.get(is_home_page=True)
                        serializer = NewsEventsSerializer(item, context={'request': request}, many=False)
                        return Response({"status": "success", "data": serializer.data})
                    except NewsEvents.DoesNotExist:
                        return Response({"status": "error", "message": "No NewsEvent with is_home_page=True found"})
                # else :
                #     try:
                #         item = NewsEvents.objects.get(is_home_page=False)
                #         serializer = NewsEventsSerializer(item, context={'request': request}, many=False)
                #         return Response({"status": "success", "data": serializer.data})
                #     except NewsEvents.DoesNotExist:
                #         return Response({"status": "error", "message": "No NewsEvent with is_home_page=False found"})
            else:
                item = NewsEvents.objects.all()
                serializer = NewsEventsSerializer(item, context={'request': request}, many=True)
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
        if 'is_home_page' in request.query_params:
            if request.query_params['is_home_page'].lower() == 'true':
                try:
                    item = Gallery.objects.get(is_home_page=True)
                    serializer = GallerySerializer(item, context={'request': request}, many=False)
                    return Response({"status": "success", "data": serializer.data})
                except Gallery.DoesNotExist:
                    return Response({"status": "error", "message": "No Gallery with is_home_page=True found"})
        else:
            item = Gallery.objects.all()
            serializer = GallerySerializer(item, context={'request':request} ,many=True)
            return Response({"status":"success","data":serializer.data})
