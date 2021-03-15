from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from contacts.models import Contact

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]                                
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, "Success")
            return redirect("dashboard")
        elif user is None:
            messages.error(request, "")
    return render(request, "accounts/login.html")

def register(request):
    if request.method == "POST":
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        password2 = request.POST["password2"]

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username")
                return redirect("register")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "")
                return redirect("register")
            elif password == password2:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)

                """
                auth.login(request, user)
                messages.success(request, "Success")
                return redirect("index")
                """

                user.save()
                messages.success(request, "Success")
                return redirect("login")
        elif password != password2:
            messages.error(request, "Password")
            return redirect("register")
    return render(request, "accounts/register.html")

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        
    return redirect("index")

def dashboard(request):
    user = request.user
    user_contacts = Contact.objects.order_by("-contact_date").filter(user_id=user.id)
    context = {
        "user": user,
        "user_contacts": user_contacts
    }
    return render(request, "accounts/dashboard.html", context)
