import os

def populate():
	dow_company = add_company('Dow')

	count = 0
	while count < 3:
		add_job(dow_company, 'Engineer {0}'.format(count))
		count += 1
	
	dupont_company = add_company('DuPont')

	while count < 5:
		add_job(dupont_company, 'Engineer {0}'.format(count))
		count += 1

	exxon_company = add_company('Exxon')
	
	while count < 10:
		add_job(exxon_company, 'Engineer {0}'.format(count))
		count += 1
	
	for company in Company.objects.all():
		for job in Job.objects.filter(company=company):
			print "{0} - {1}".format(company, job)

def add_company(name):
	return Company.objects.get_or_create(name=name)[0]

def add_job(company, title):
	return Job.objects.get_or_create(company=company, title=title)[0]

if __name__ == "__main__":
	print "Populating the database..."
	os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'open_database.settings')
	from open.models import Company, Job
	populate()
	print "Done"
