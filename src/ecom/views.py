from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model
from .forms import ContactForm, LoginForm, RegisterForm


def login_page(request):
    form = LoginForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            print(request.user.is_authenticated)
            if user is not None:
                login(request, user)
                return redirect('login')
            else:
                print('error')
    return render(request, 'auth/login.html', {'form': form})


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form1 = ContactForm(request.POST)
        if form1.is_valid():
            print(form1.cleaned_data)
        print(request.POST.get('content', 'test'))
    context = {
        'form': form,
        'title': 'Contact Form'
    }
    return render(request, 'contact/view.html', context)


User = get_user_model()


def register_view(request):
    form = RegisterForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            new_user = User.objects.create_user(
                username=username, password=password, email=email)
            print(new_user)
    return render(request, 'auth/register.html', {'form': form})
