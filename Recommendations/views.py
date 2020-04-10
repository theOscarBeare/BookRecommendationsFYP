from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import ListAPIView
from .models import *
from .serializer import *


class Allenduser(ListAPIView):

    queryset = enduser.objects.all()
    serializer_class = enduserSerializer

    def post(self, request, format=None):
        serializer = enduserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class enduserView(APIView):

    def get(self, request, pk, format=None):
        try:
            tech = enduser.objects.get(pk=pk)
            serializer = enduserSerializer(tech)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        tech = enduser.objects.get(pk=pk)
        tech.delete()
        return Response(status=status.HTTP_200_OK)


class Alluserinformation(ListAPIView):

    queryset = userinformation.objects.all()
    serializer_class = userInformationSerializer

    def post(self, request, format=None):
        serializer = userInformationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userinformationView(APIView):

    def get(self, request, pk, format=None):
        try:
            tech = userinformation.objects.get(pk=pk)
            serializer = userInformationSerializer(tech)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        tech = userinformation.objects.get(pk=pk)
        tech.delete()
        return Response(status=status.HTTP_200_OK)


class Alluserrecomendations(ListAPIView):

    queryset = userrecommendations.objects.all()
    serializer_class = userrecommendations

    def post(self, request, format=None):
        serializer = userRecommendationsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class userRecommendationsView(APIView):

    def get(self, request, pk, format=None):
        try:
            tech = userrecommendations.objects.get(pk=pk)
            serializer = userRecommendationsSerializer(tech)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, format=None):
        tech = userrecommendations.objects.get(pk=pk)
        tech.delete()
        return Response(status=status.HTTP_200_OK)
