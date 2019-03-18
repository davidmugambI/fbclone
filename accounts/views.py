from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm,\
    UserChangeForm, PasswordChangeForm
from .forms import RegistrationForm, EditProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
# add
from django.contrib import messages

# Note deactivation of the login required due to use of custom middleware

# Create your views here.
#@login_required
def home(request):
    user = request.user
    #numbers = [1,2,3,5]
    #name = 'David'
    #return HttpResponse('Home Page')
    #args ={'myname': name,'numbers':numbers }
    return render(request, 'account/home.html', {'user':user})

def login_redirect(request):
    return redirect('/accounts/login') # takes u to login page wen \
    # u try to access home b4 logging in
'''
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/accounts/')
    else:
        form = UserCreationForm()
        args = {'form': form}
        return render(request, 'accounts/reg_form.html',args)
'''

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')
    else:
        form = RegistrationForm()
    args = {'form': form}
    return render(request, 'account/reg_form.html',args)

#@login_required
def view_profile(request,pk=None):
    if pk:
        user = User.objects.get(pk=pk)
    else:
        user = request.user
    #args = {'user': request.user}
    args = {'user': user}
    return render(request, 'account/profile.html', args)

'''
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('/accounts/profile')
    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'accounts/edit_profile.html', args)
'''
#@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST,instance=request.user)

        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'account/edit_profile.html', args)

#@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST,user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('profile')
        else:
            return redirect('/accounts /')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'account/change_password.html', args)
