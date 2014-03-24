from django import forms
from open.models import Company, Job, UserProfile
from django.contrib.auth.models import User

class UserProfileForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = '__all__'

class CompanyForm(forms.ModelForm):
	
	class Meta:
		model = Company
		fields = '__all__'
		labels = {
				'name': 'Company Name',
				'website': 'Company Website',
				}
		help_text = {
				'name': "Please enter the company name",
				}
		error_messages = {
				'name': {
					'max_length': "This company name is too long",
					}
				NON_FIELD_ERRORS: {
					'unique_together': "%(model_name)\'s %(field_labels)s are not unique.",
					}
				}
	
class JobForm(forms.ModelForm):

	class Meta:
		model = Job
		fields = '__all__'
		widgets = {
				'company': forms.Select(choices=Company.objects.all()),
				}
		labels = {
				'company': 'Company',
				'title': 'Job Title',
				'location': 'Job Location',
				'description': 'Job Description',
				'salary': 'Job Salary',
				'job_website': 'Job Website',
				'posted_date': 'Posted Date',
				'deadline': 'Application Deadline',
				}
		error_messages = {
				}
