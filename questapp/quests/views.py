from django.shortcuts import render
from .models import Quest, Strength, Endurance, Wisdom, User
from rest_framework import viewsets
from rest_framework import permissions
# from .serializers import QuestSerializer
class QuestViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Quest.objects.all()
    # The serializer class for serializing output
    serializer_class = QuestSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]

class StrengthViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Strength.objects.all()
    # The serializer class for serializing output
    serializer_class = StrengthSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]

class EnduranceViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Endurance.objects.all()
    # The serializer class for serializing output
    serializer_class = EnduranceSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]

class WisdomViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = Wisdom.objects.all()
    # The serializer class for serializing output
    serializer_class = WisdomSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]

class UserViewSet(viewsets.ModelViewSet):
    ## The Main Query for the index route
    queryset = User.objects.all()
    # The serializer class for serializing output
    serializer_class = UserSerializer
    # optional permission class set permission level
    permission_classes = [permissions.AllowAny] #Coule be [permissions.IsAuthenticated]
