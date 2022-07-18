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
from tattoo.views import Tattoo
from tattoo.serializers import TattooSerializer
from users.models import User
from transaction.models import Transaction
from transaction.serializers import TransactionSerializer
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
    # def get(self,request,format=None,user_id=None):
    #     try:
    #         print(user_id)
    #         tattoo = Tattoo.objects.all().order_by('-numAvail')
    #         serializers = TattooSerializer(tattoo,many=True)
    #         for x in serializers.data:
    #             user = User.objects.filter(id=x['user_id'])
    #             user = UserSerializer(user,many=True)
    #             x['email']= user.data[0]['email']
    #             x['firstname']= user.data[0]['firstname']
    #             x['lastname']= user.data[0]['lastname']
    #         return Response(data=serializers.data)
    #     except Exception as e:
    #         print(e)
    #         return Response(status=status.HTTP_404_NOT_FOUND,data=[])

    # class TattooMostBuy(generics.GenericAPIView):
    # def get(self,request,format=None,user_id=None):
        # try:
        #     print(user_id)
        #     product = Product.objects.all().order_by('-numBuy')
        #     serializers = TransactionSerializer(transaction_items,many=True)
        #     print(serializers.data)
        #     return Response(data=serializers.data)
        # except Exception as e:
        #     print(e)
        #     return Response(status=status.HTTP_404_NOT_FOUND,data=[])
        def get(self,request,format=None,user_id=None):
            print("yes1")
            try:
                isHave = False
                if(len(request.query_params.get('date').split(','))==2):
                    listItem = request.query_params.get('date').split(',')
                    userItem = Tattoo.objects.all()
                    userItem = TattooSerializer(userItem,many=True)
                    for x in userItem.data:
                        artistItem = Transaction.objects.filter(design_id=x['id'],transaction_date__gte=f'{listItem[0]} 00:00:00',transaction_date__lte=f'{listItem[1]} 23:59:00').count()
                        x['numberOfTransaction'] = artistItem
                        if(artistItem!=0):
                            isHave = True
                        print(artistItem)
                    items = sorted(userItem.data, key=lambda d: d['numberOfTransaction'],reverse=True)
                    if(isHave):
                        return Response(data=items)
                    else:
                        return Response(data=[])

                if(request.query_params.get('date')==''):
                    userItem = Tattoo.objects.all()
                    userItem = TattooSerializer(userItem,many=True)
                    for x in userItem.data:
                        artistItem = Transaction.objects.filter(design_id=x['id']).count()
                        x['numberOfTransaction'] = artistItem
                        if(artistItem!=0):
                            isHave = True
                    items = sorted(userItem.data, key=lambda d: d['numberOfTransaction'],reverse=True)
                    if(isHave):
                        return Response(data=items)
                    else:
                        return Response(data=[])
                else:
                    print("yes")
                    userItem = Tattoo.objects.all()
                    userItem = TattooSerializer(userItem,many=True)
                    for x in userItem.data:
                        artistItem = Transaction.objects.filter(design_id=x['id'],transaction_date__gte=f'{request.query_params.get("date")} 00:00:00',transaction_date__lte=f'{request.query_params.get("date")} 23:59:00').count()
                        x['numberOfTransaction'] = artistItem
                        if(artistItem!=0):
                            isHave = True
                    items = sorted(userItem.data, key=lambda d: d['numberOfTransaction'],reverse=True)
                    if(isHave):
                        return Response(data=items)
                    else:
                        return Response(data=[])
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