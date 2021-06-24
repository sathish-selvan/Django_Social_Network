from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from profiles.models import Profile
from django.contrib.auth.models import User

def home_veiw(request):
    user  = request.user

    context = {
        "hello" : "hello",
        'user' : user
    }
    return render(request, "main/home.html", context)
    # return HttpResponse("Hello world")

def seach_friend(request):
    if request.method == "GET":
        name = request.GET.get("q")
        user = get_object_or_404(User, username=name)
        
        profile = get_object_or_404(Profile, user=user)
        print(profile)

        return redirect(profile.get_absolute_url())
