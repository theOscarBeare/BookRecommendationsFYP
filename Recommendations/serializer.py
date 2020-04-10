from rest_framework import serializers
from .models import enduser, userinformation, userrecommendations


class enduserSerializer(serializers.ModelSerializer):

    class Meta:
        model = enduser
        fields = '__all__'


class userRecommendationsSerializer(serializers.ModelSerializer):

    class Meta:
        model = userrecommendations
        fields = '__all__'


class userInformationSerializer(serializers.ModelSerializer):

    class Meta:
        model = userinformation
        fields = '__all__'
