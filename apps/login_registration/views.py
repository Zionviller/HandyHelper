from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt

def index(request):
    print('\n\n** Index')
    if not 'logged_in' in request.session:
        request.session['logged_in'] = False
    elif request.session['logged_in'] == True:
        return redirect('/dashboard')

    return render(request, 'login_registration/index.html')

def register(request):
    print('\n\n** Register')
    print(request.POST)

    errors = User.objects.validateNewUser(request.POST)

    if len(errors):
        print("There are errors! I can't register that! GeddaddaHERE!")
        for k, message in errors.items():
            messages.error(request, message)
        return redirect('/')
    else:
        pwHash = bcrypt.hashpw(request.POST['password'].encode('utf-8'), bcrypt.gensalt(12))
        user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], pass_hash = pwHash.decode())
        print(user)
        print("Nice.. you're registered.")
        request.session['logged_in'] = True
        request.session['user_id'] = user.id
        return redirect('/')

def login(request):
    print('\n\n** Login')
    print(request.POST)

    errors = User.objects.validateLogin(request.POST)

    if len(errors):
        for k, message in errors.items():
            messages.error(request, message)
        return redirect('/')
    else:
        u = User.objects.get(email = request.POST['email'])

        request.session['logged_in'] = True
        print(f'HERE!! This is the user object: { u }')
        request.session['user_id'] = u.id
        return redirect('/')

def success(request):
    print("Getting the User to show as successful...")
    u = User.objects.get(id=request.session["user_id"])
    print(f'User: {u}')

    context = {
        'full_name' : f'{u.first_name}'
    }

    return render(request, 'login_registration/success.html', context)

def logout(request):
    request.session['logged_in'] = False
    request.session['user_id'] = None
    return redirect('/')
