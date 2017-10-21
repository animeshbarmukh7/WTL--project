from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.shortcuts import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('alltracks')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})


def about(request):
    context = {}
    template = 'about.html'
    return render(request,template,context)

@login_required
def userProfile(request):
	user = request.user
	profile = Profile.objects.get_or_create(user=user)[0]
	context = {'user':user,
				'profile':profile,
	}
	template = 'profile.html'
	return render(request,template,context)


def logout_view(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Successfully Logged Out')
    return HttpResponseRedirect('/login/')

def home(request):
    context = {}
    template = 'home.html'
    return render(request,template,context)

def edit_profile(request):
    context = {}
    user = request.user
    profile = Profile.objects.get_or_create(user=user)[0]
    if request.method == "POST":
	    user.first_name= request.POST['first_name']
	    user.last_name= request.POST['last_name']
	    profile.phone_no= request.POST['phone_no']
	    profile.secondary_no= request.POST['secondary_no']
	    profile.address= request.POST['address']
	    profile.f_name=request.POST['f_name']
	    profile.m_name=request.POST['m_name']
	    profile.dob=request.POST['dob']
	    user.save()
	    profile.save()
		
	    return redirect("/profile")
		
    else:
	    context['first_name']=user.first_name
	    context['last_name']=user.last_name
	    context['phone_no']=profile.phone_no
	    context['secondary_no'] = profile.secondary_no
	    context['address'] = profile.address
	    context['f_name']=profile.f_name
	    context['m_name']=profile.m_name
	    context['dob']=profile.dob


    return render(request,'edit_profile.html',context)