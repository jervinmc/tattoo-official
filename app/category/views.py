from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Category
from .serializers import CategorySerializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
class CategoryView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Category.objects.all()
    serializer_class=CategorySerializer



class CategoryUserID(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            print(user_id)
            Category = Category.objects.filter(user_id=user_id)
            serializers = CategorySerializer(Category,many=True)
            print(serializers.data)
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])
