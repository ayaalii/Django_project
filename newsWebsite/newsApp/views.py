from django.shortcuts import render, get_object_or_404
from .models import Post , Comment
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect,HttpResponse
from django.template import RequestContext
from newsApp.forms import *
# Create your views here.

def homePageForUser(request):
	posts = Post.objects.order_by('-date')
	context = {'posts':posts}
	return render(request,'newsApp/homePageForUser.html',context)

def postDetails(request , post_id):
	post = get_object_or_404( Post, id=post_id)
	comments = Comment.objects.filter(post=post_id)
	context = {'post':post,'comments':comments}
	return render(request,'newsApp/postDetails.html',context)



@csrf_protect
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
            username=form.cleaned_data['username'],
            password=form.cleaned_data['password1'],
            email=form.cleaned_data['email']
            )
            return HttpResponseRedirect('/register/success/')
    else:
        form = RegistrationForm()
    variables = RequestContext(request, {
    'form': form
    })
   
    return render_to_response(
    'registration/register.html',
    variables,
    )
 
def register_success(request):
    return render_to_response(
    'registration/success.html',
    )
 
def logout_page(request):
    logout(request)
    return HttpResponseRedirect('/')



