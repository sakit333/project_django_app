# from django.shortcuts import render, HttpResponse

# def index(request):
#     print(request)
#     return render(request, 'index.html')

# def login(request):
#     print(request)
#     return render(request, 'login.html')

# def home(request):
#     print(request)
#     return render(request, 'home.html')


from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password, check_password
from .forms import SignUpForm, LoginForm
from .models import UserProfile

def home(request):
    return render(request, 'home.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = make_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = UserProfile.objects.get(username=username)
            if check_password(password, user.password):
                # Authentication successful, redirect to home or some other page
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
