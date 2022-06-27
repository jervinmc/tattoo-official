from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Transaction
from .serializers import TransactionSerializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
import requests
from tattoo.models import Tattoo
from django.db.models import F
from cart.models import Cart
import json
class TransactionView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer
    def create(self,request):
        res = request.data
        Tattoo.objects.filter(id=res.get('design_id')).update(numAvail=F('numAvail')+1)
        serializer = TransactionSerializer(data=res)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(data=serializer.data)



class TransactionUserArtistID(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            print(user_id)
            transaction_items = Transaction.objects.filter(artist_id=user_id)
            serializers = TransactionSerializer(transaction_items,many=True)
            print(serializers.data)
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

class TattooMostBuy(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            print(user_id)
            product = Product.objects.all().order_by('-numBuy')
            serializers = TransactionSerializer(transaction_items,many=True)
            print(serializers.data)
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

class TransactionUserClientID(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            print(user_id)
            transaction_items = Transaction.objects.filter(user_id=user_id)
            serializers = TransactionSerializer(transaction_items,many=True)
            print(serializers.data)
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

class TransactionPayMaya(generics.GenericAPIView):
    def post(self,request,format=None):
        try:
            res = request.data
            url = "https://pg-sandbox.paymaya.com/checkout/v1/checkouts"
            payload = {
                "totalAmount": {
                    "value": res.get('price'),
                    "currency": "PHP"
                },
                "buyer": {
                    "billingAddress": {"countryCode": "GB"},
                    "shippingAddress": {"countryCode": "GB"},
                    "firstName": "Juan",
                    "middleName": "D",
                    "lastName": "Delacruz",
                    "birthday": "2019-10-19"
                },
                "items": [
                    {
                        "amount": {"value": res.get('price')},
                        "totalAmount": {"value": res.get('price')},
                        "name": 'test',
                        "quantity": "1",
                        "code": "uus",
                        "description": "dse"
                    }
                ],
                "requestReferenceNumber": "123123"
            }
            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
                "Authorization": "Basic cGstWjBPU3pMdkljT0kyVUl2RGhkVEdWVmZSU1NlaUdTdG5jZXF3VUU3bjBBaDo="
            }

            response = requests.post(url, json=payload, headers=headers)
            print(response.text)
            return Response(data=json.loads(response.text))
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])



class TransactionBulkAdd(generics.GenericAPIView):
    def post(self,request):
        res = request.data
        for x in res.get('data'):
            Tattoo.objects.filter(id=x['design_id']).update(numAvail=F('numAvail')+1)
            x['status']='Pending'
            serializer = TransactionSerializer(data=x)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        Cart.objects.filter(user_id=res.get('user_id')).delete()
        return Response(data=serializer.data)

