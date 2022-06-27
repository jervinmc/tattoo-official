from rest_framework import serializers
from .models import Tattoo

class TattooSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tattoo
        fields="__all__"
