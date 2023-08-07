from rest_framework import serializers

from .models import category, brand, product

class categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = category
        fields = "__all__"
    
class brandSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = brand
        fields = "__all__"
        
class productSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = product
        fields = "__all__"