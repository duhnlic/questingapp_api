from django.shortcuts import render
from .models import Quest, Strength, Endurance, Wisdom, User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import QuestSerializer, StrengthSerializer, EnduranceSerializer, WisdomSerializer, UserSerializer

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
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] 
