from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from open.models import Company, Job, UserProfile
from open.forms import CompanyForm, JobForm, UserProfileForm

def index(request):
	context = RequestContext(request)
	context_dict = {}
	
	return render_to_response('open/index.html', context_dict, context)

def home(request):
	context = RequestContext(request)
	context_dict = {}
	add_company_option = {
			'url':'/open/add_company/',
			'heading':'Add a Company',
			'paragraph':'Before you can add a job, you must enter the company name for the job.',
			}
	add_job_option = {
			'url':'/open/add_job/',
			'heading':'Add a Job',
			'paragraph':'Once you have a company, you can add jobs for that company.',
			}
	edit_job_option = {
			'url':'/open/edit_job/',
			'heading':'Edit a Job',
			'paragraph': 'If you made a mistake on the job form, then you can easily fix it here.',
			}

	options = (add_company_option, add_job_option, edit_job_option)
	context_dict['options'] = options

	return render_to_response('open/home.html', context_dict, context)

def job_listing(request):
	context = RequestContext(request)
	company_list = Company.objects.all()
	context_dict = {'company_list': company_list}
	for company in company_list:
		context_dict[company.name] = Job.objects.filter(company=company)

	return render_to_response('open/job_listing.html', context_dict, context)

def add_company(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = CompanyForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect(reverse("home"))
		else:
			print form.errors
	else:
		form = CompanyForm()

	return render_to_response('open/add_company.html', {'form': form}, context)

def add_job(request):
	context = RequestContext(request)

	if request.method == 'POST':
		form = JobForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return HttpResponseRedirect(reverse("home"))
		else:
			print form.errors
	else:
		form = JobForm()
	
	return render_to_response('open/add_job.html', {'form', form}, context)

def register(request):
	pass

def profile(request):
	return HttpResponse("This is the profile page.")

def about(request):
	return HttpResponse("This is the about page.")
