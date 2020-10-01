from rest_framework import serializers
from . import models


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'FirstName', 'LastName', 'EmailAddress', 'ConfirmEmailAddress', 'Password', 'ConfirmPassword', 'created_at', 'updated_at',)
        model = models.Post