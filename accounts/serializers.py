from pyexpat import model
from attr import fields
from rest_framework import serializers
from .models import *

class profileserializer(serializers.ModelSerializer):
    class Meta:
        model=Profile
        fields="__all__"


class commentserializer(serializers.ModelSerializer):
    class Meta:
        model=Comment
        fields="__all__"