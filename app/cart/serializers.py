from rest_framework import serializers
from .models import Cart

class Carterializer(serializers.ModelSerializer):
    class Meta:
        model=Cart
        fields="__all__"
