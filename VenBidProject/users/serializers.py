from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profile
        fields = ('user', 'companyname', 'mobileno', 'telephone', 'addresslane1', 'addresslane2', 'city')