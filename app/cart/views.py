from django.shortcuts import render
from rest_framework import viewsets,generics
from .models import Cart
from .serializers import Carterializer
from rest_framework import filters
from rest_framework import status, viewsets
from rest_framework.response import Response
from django.db.models import F
class CartView(viewsets.ModelViewSet):  
    filter_backends = [filters.SearchFilter]
    search_fields = ['category','price','name','descriptions']
    queryset=Cart.objects.all()
    serializer_class=Carterializer
    
    # def create(self,request):
    #     res = request.data
    #     item_val = Cart.objects.filter(user_id = res.get('user_id'),product_id = res.get('product_id')).count()
    #     Product.objects.filter(id=res.get('product_id')).update(stocks=F('stocks')-res.get('quantity'))
    #     item_inv = Product.objects.filter(id=res.get('product_id'))
    #     serializer = ProductSerializer(item_inv,many=True)
    #     inventory_serializer = InventoryReportSerializer(data={"product_name":res.get('product_name'),"status":"Subtract","stocks":res.get('quantity'),"remaining_stocks":serializer.data[0]['stocks'],"module":"products"})
    #     # Product.objects.filter(id=res.get('product_id')).update(numBuy=F('numBuy')+res.get('quantity'))
    #     if(item_val>0):
    #         Cart.objects.filter(user_id = res.get('user_id'),product_id = res.get('product_id')).update(quantity = F('quantity') + res.get('quantity'))
    #     else:
    #         print("okay")
    #         ser = Carterializer(data=res)
    #         ser.is_valid(raise_exception=True)
    #         ser.save()
    #     return Response()




class CartUserID(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            items = Cart.objects.filter(user_id=user_id)
            listitem = []
            serializers = Carterializer(items,many=True)
            # for x in serializers.data:
            #     print(x['product_id'])
            #     item = Product.objects.filter(id=x['product_id'])
            #     item = ProductSerializer(item,many=True)
            #     x['price'] = item.data[0]['price']
            #     print(x['price'])
            return Response(data=serializers.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])



class TransactionBulkDelete(generics.GenericAPIView):
    def get(self,request,format=None,user_id=None):
        try:
            Cart.objects.filter(user_id=user_id).delete()
            return Response(data=[])
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND,data=[])

