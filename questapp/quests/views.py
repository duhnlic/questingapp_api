from django.shortcuts import render
from .models import Quest, Strength, Endurance, Wisdom, User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import QuestSerializer, StrengthSerializer, EnduranceSerializer, WisdomSerializer, UserSerializer
from rest_framework import serializers

class QuestViewSet(viewsets.ModelViewSet):
    queryset = Quest.objects.all()
    serializer_class = QuestSerializer
    permission_classes = [permissions.AllowAny] 

class StrengthViewSet(viewsets.ModelViewSet):
    queryset = Strength.objects.all()
    serializer_class = StrengthSerializer
    permission_classes = [permissions.AllowAny] 

class EnduranceViewSet(viewsets.ModelViewSet):
    queryset = Endurance.objects.all()
    serializer_class = EnduranceSerializer
    permission_classes = [permissions.AllowAny] 

class WisdomViewSet(viewsets.ModelViewSet):
    queryset = Wisdom.objects.all()
    serializer_class = WisdomSerializer
    permission_classes = [permissions.AllowAny] 

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    def get_queryset(self):
        queryset = User.objects.all()
        print(self.request)
        print("This is Console Testing")
        return queryset

    def perform_create(self, serializer):   
        queryset = User.objects.filter(username=self.request.data["username"])
        if queryset.exists():
            raise serializers.ValidationError('You have already signed up')
        serializer.save(username=self.request.data["username"])

    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] 
