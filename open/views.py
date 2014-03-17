from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from open.models import Company, Job

def index(request):
	context = RequestContext(request)
	context_dict = {}
	
	return render_to_response('index.html', context_dict, context)

def home(request):
	context = RequestContext(request)
	company_list = Company.objects.all()
	context_dict = {'company_list': company_list}

	return render_to_response('home.html', context_dict, context)

def profile(request):
	return HttpResponse("This is the profile page.")

def about(request):
	return HttpResponse("This is the about page.")
