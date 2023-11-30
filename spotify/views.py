from django.shortcuts import render, redirect
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Songs
from .serializers import songserials
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib import messages
from rest_framework.permissions import IsAdminUser


# Create your views here.

# def admin_only(User):
#     return User.is_authenticated and User.is_superuser

def login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.info(request, "Logged in successfully")
            return redirect("/")
        else:
            messages.info(request, "Credentials Invalid")
            return redirect("login")
    return render(request, "spotify/login.html")



def register(request):
    if request.method == 'POST':
        username = request.POST.get("USERNAME")
        email = request.POST.get("EMAIL")
        password = request.POST.get("PASSWORD")
        password2 = request.POST.get("PASSWORD2")

        print(username, email, password, password2)

        if password != password2:
            messages.info (request, "Password doesn't match")
            return redirect('signup')
        else:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return redirect("signup")
            elif User.objects.filter(username=username).exists():
                messages.info(request, "Username already taken")
                return redirect("signup")
            else:
                user = User.objects.create_user(username=username, email=email)
                user.set_password(password)
                user.save()
                return redirect("login")
    elif request.method == "GET":
            return render(request, 'spotify/sign_up.html')
    return render(request, "spotify/sign_up.html")


@login_required
@api_view(["GET", "POST"])
def User_view(request):
    if request.method == "GET":
        songs_get = Songs.objects.all()
        serialized_songs = songserials(songs_get, many=True)
        return Response(serialized_songs.data)
    else: 
        new_song = songserials(data=request.data)
        if new_song.is_valid():
            new_song.save()
            return Response("Song added successfully")
        return Response(new_song.errors)
    
# @user_passes_test(admin_only)
@permission_classes([IsAdminUser])
@api_view(["GET", "PUT","DELETE"])
def Admin_view(request, id):
    if request.method == "GET":
        single_songs = Songs.objects.get(id=id)
        serialized_song = songserials(single_songs)
        return Response(serialized_song.data)
    elif request.method == "PUT":
        single_song = Songs.objects.get(id=id)
        serial_song = songserials(single_song, data=request.data, partial=True)
        if serial_song.is_valid():
            serial_song.save()
            return Response("You have successfully updated this song")
        return Response("Something went wrong!!")
    else:
        songs_serials = Songs.objects.get(id=id)
        songs_serials.delete()
        return Response("You have successfully deleted this song")