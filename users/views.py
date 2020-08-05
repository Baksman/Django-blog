from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user_name = form.cleaned_data.get("username")
            messages.success(request,f"created an account for {user_name}")
            return redirect("blog-home")
    else:
        form = UserRegisterForm()
    return render(request,"users/register.html",{"form":form})