from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import videoSerializer  
from pyffmpeg import FFmpeg
# from .status_url import stock_url
import os
from rest_framework.authentication import TokenAuthentication,BasicAuthentication,SessionAuthentication
from .models import Videomodel
from users.models import MyUser
from rest_framework.permissions import IsAuthenticated
from django.conf import settings
from django.http import JsonResponse
# Create your views here.
import cv2
from .video_genrator import GenrateVideo
from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size = 10

# def get_video_resolution(video_path):
#     cap = cv2.VideoCapture(video_path)
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     cap.release()
#     return (width, height)

class Index(APIView):
    permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,BasicAuthentication,SessionAuthentication)
    
    pagination_class = MyPagination()
    def get(self, request, format=None):
        print(settings.BASE_DIR)
        queryset=Videomodel.objects.filter(user=request.user)
        paginated_queryset = self.pagination_class.paginate_queryset(queryset, request)
        serializer = videoSerializer(paginated_queryset, many=True)
        return self.pagination_class.get_paginated_response(serializer.data)
                                     
    def post(self, request, format=None):
        serializer = videoSerializer(data=request.data )
        if serializer.is_valid(): 
            ser=serializer.save()
            video=str(settings.BASE_DIR)+serializer.data['video']
            img_logo=str(settings.BASE_DIR)+serializer.data['logo']
            context=serializer.data['content']
            usr=MyUser.objects.get(email=request.user.email)
            usr_img=usr.profile.path
            output_file=f'media/final_video/out_{ser.id}.mp4'
            GenrateVideo(video,img_logo,context,usr_img,usr.name,output_file)
            obj=Videomodel.objects.get(id=ser.id)
            removeable_video=obj.video.path
            obj.video=f'final_video/out_{ser.id}.mp4'
            obj.user=request.user
            obj.save()
            ser=videoSerializer(instance=obj,many=False)
            # delete fun
            if os.path.exists(removeable_video):
                os.remove(removeable_video)
            return Response({"status": "success", "data": ser.data}, status=status.HTTP_200_OK) 
        else:  
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)  
        



