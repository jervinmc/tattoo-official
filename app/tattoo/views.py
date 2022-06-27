from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Tattoo
from .serializers import TattooSerializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
from category.models import Category
from category.serializers import CategorySerializer
from users.serializers import UserSerializer
from users.models import User
class TattooView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Tattoo.objects.all()
    serializer_class=TattooSerializer

  

class TattooUserID(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            print(user_id)
            tattoo = Tattoo.objects.filter(user_id=user_id)
            serializers = TattooSerializer(tattoo,many=True)
            print(serializers.data)
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

class CategoryDesign(generics.GenericAPIView):
    def get(self,request,format=None,category_name=None):
        try:
            items = Tattoo.objects.filter(category=category_name)
            items = TattooSerializer(items,many=True)
            return Response(data=items.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

class TattooMarket(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            listitem = []
            category_items = Category.objects.all()
            category_serializers = CategorySerializer(category_items,many=True)
            for x,index in enumerate(category_serializers.data):
                listitem.append({"category_name":index['category_name'],"tattoo_list":[]})
                tattoo_items=Tattoo.objects.filter(category=index['category_name'],status='Approved')
                tattoo_serializers = TattooSerializer(tattoo_items,many=True)
                for i in tattoo_serializers.data:
                    user = User.objects.filter(id=i['user_id'])
                    serializer = UserSerializer(user,many=True)
                    i['gcash'] = serializer.data[0]['gcash']
                    print(i['gcash'])
                    listitem[x]['tattoo_list'].append(i)

            return Response(data=listitem)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])


class TattooMostBuy(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            print(user_id)
            tattoo = Tattoo.objects.all().order_by('-numAvail')
            serializers = TattooSerializer(tattoo,many=True)
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])


class TattooMarketArtist(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            listitem = []
            category_items = Category.objects.all()
            category_serializers = CategorySerializer(category_items,many=True)
            for x,index in enumerate(category_serializers.data):
                listitem.append({"category_name":index['category_name'],"tattoo_list":[]})
                tattoo_items=Tattoo.objects.filter(category=index['category_name'],status='Approved',user_id=user_id)
                tattoo_serializers = TattooSerializer(tattoo_items,many=True)
                for i in tattoo_serializers.data:
                    listitem[x]['tattoo_list'].append(i)

            return Response(data=listitem)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])