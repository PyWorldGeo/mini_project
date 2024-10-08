from django.shortcuts import render, redirect
from .models import Name, User, Type
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MyUserCreationForm, NameForm, UserForm
from django.db.models import Q

# Create your views here.
def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ""
    names = Name.objects.filter(Q(name__icontains=q) | Q(description__icontains=q) | Q(type__type__icontains=q))

    # names = Name.objects.all()
    context = {"names": names}

    return render(request, 'base/home.html', context)

def login_page(request):
    #ბოლოს
    page = "login"
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "User doesn't exist!")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or Password doesn't exist!")

    context = {"page": page}
    return render(request, "base/login_register.html", context)



def logout_user(request):
    logout(request)
    return redirect('home')

def register_page(request):
    form = MyUserCreationForm()
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "An error occurred during registration")

    return render(request, 'base/login_register.html', {'form': form})


def add_note(request):
    types = Type.objects.all()

    form = NameForm()
    if request.method == "POST":
        form = NameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            messages.error(request, "Book Already Exists!")

    return render(request, 'base/add_name.html', {'form': form, 'types': types})




def delete_note(request, id):
    name = Name.objects.get(id=id)

    if request.method == "POST":
        name.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': name})


@login_required(login_url='login')
def update_user(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == "POST":
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, "base/update-user.html", {'form': form})



