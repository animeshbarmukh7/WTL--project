from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import profile
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
#from .forms import EditInfo
from django.contrib.auth.forms import UserChangeForm
from django.views.generic import View

# Create your views here.
def home(request):
	context = {}
	template = 'home.html'
	return render(request,template,context)

def about(request):
	context = {}
	model = profile
	template = 'about.html'
	return render(request,template,context)

'''@login_required
def edit_profile(request):
	if request.method=="POST":
		print ("POST\n")
		form=EditInfo(request.POST)
		if form.is_valid():
			print("Valid")
			post=form.save(commit=False)
			post.user=request.user
			post.save()
		return HttpResponseRedirect('/profile/')


	else:
		form=EditInfo()
		template = 'edit_profile.html'
		context={'form':form}
		return render(request,template,context)

class Edit_profile(View):
    form_class = EditInfo
    template_name = 'edit_profile.html'


    # Display blank form
    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            album = form.save(commit=False)  # we are not actually stroing in the database
            album.save()
'''
@login_required
def userProfile(request):
	user = request.user
	context = {'user':user}
	template = 'profile.html'
	return render(request,template,context)
