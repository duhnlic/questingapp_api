from django.shortcuts import render,redirect
from .models import Quest, Strength, Endurance, Wisdom, User
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import QuestSerializer, StrengthSerializer, EnduranceSerializer, WisdomSerializer, UserSerializer
from rest_framework import serializers
from django.contrib.auth import login, authenticate
from .forms import RegisterForm

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
    def perform_create(self, serializer):  
        User(username=self.request.data["username"]).save()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny] 

def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
        return redirect("/home")
    else:
        form = RegisterForm()
    return render(response, "register/register.html", {"form":form})