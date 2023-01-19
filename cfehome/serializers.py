from rest_framework import serializers
from .models import Drink
class DrinkSerializer(serializers.ModelSerializer):
    #Meta class describing the drink
    class Meta:
        model = Drink
        fields =['id','name','description']
        
        
    