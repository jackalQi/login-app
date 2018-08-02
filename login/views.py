from django.shortcuts import render, redirect
from .models import User
from .forms import UserForm, RegisterForm
# Create your views here.


def login(request):
    if request.session.get("is_login", None):
        return redirect("/index/")
    if request.method == "POST":
        user_form = UserForm(request.POST)
        # username = request.POST.get("username", None)
        # password = request.POST.get("password", None)
        message = "username and password required!"
        if user_form.is_valid():
            username = user_form.cleaned_data['username']
            password = user_form.cleaned_data['password']
        try:
            user = User.objects.get(name=username)
            if password == user.password:
                request.session['is_login'] = True
                request.session['id'] = user.pk
                request.session['name'] = user.name
                return redirect("/index/")
            else:
                message = "Wrong password"
        except:
            message = "No user"
        return render(request, "login/login.html", locals())
    user_form = UserForm()
    return render(request, "login/login.html", locals())


def index(request):
    pass
    return render(request, "login/index.html")


def logout(request):
    if not request.session.get("is_login", None):
        return redirect("/index/")
    request.session.flush()
    return redirect("/index/")


def register(request):
    if request.session.get("is_login", None):
        return redirect("/index/")
    if request.method == "POST":
        register_form = RegisterForm(request.POST)
        message = "Check information"
        if register_form.is_valid():
            username = register_form.cleaned_data["username"]
            password1 = register_form.cleaned_data["password1"]
            password2 = register_form.cleaned_data["password2"]
            email = register_form.cleaned_data["email"]
            sex = register_form.cleaned_data["sex"]
            if password1 != password2:
                message = "password problem"
                return render(request, 'login/register.html', locals())
            else:
                user = User.objects.filter(name=username)
                if user:
                    message = "already have username"
                    return render(request, "login/register.html", locals())
                check_email = User.objects.filter(email=email)
                if check_email:
                    message = "email"
                    return render(request, "login/register.html", locals())

                new_user = User()
                new_user.name = username
                new_user.password = password1
                new_user.email = email
                new_user.sex = sex
                new_user.save()
                return redirect("/login/")
    register_form = RegisterForm()
    return render(request, 'login/register.html', locals())
