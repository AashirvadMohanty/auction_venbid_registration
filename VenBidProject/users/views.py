from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from users.forms import SignUpForm

from rest_framework import generics

from . import models
from . import serializers

class UserListView(generics.ListAPIView):
    queryset = models.Profile.objects.all()
    serializer_class = serializers.UserSerializer

@login_required
def home(request):
    return render(request, 'main/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.save()
            # username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            confirm_email = form.cleaned_data.get('email')
            user = authenticate(username=user.username, password=raw_password, email=confirm_email)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'main/signup.html', {'form': form})