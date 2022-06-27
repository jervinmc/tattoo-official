from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Design
from .serializers import DesignSerializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
from category.models import Category
from category.serializers import CategorySerializer
class DesignView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    queryset=Design.objects.all()
    serializer_class=DesignSerializer

  

class DesignUserID(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            design = Design.objects.filter(user_id=user_id)
            serializers = DesignSerializer(design,many=True)
            print(serializers.data)
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
