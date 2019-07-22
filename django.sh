# Set virtualenv
sudo apt install virtualenv
virtualenv django
source django/bin/activate

# Install python and django (with D Mayus)
sudo apt install python3
pip3 install Django
python3 -m django --version

# Create a project
django-admin startproject myproject
python3 manage.py runserver

# Create app in project
python3 manage.py startapp polls

# Configure db in setting.py and create db's to the installed apps
python3 manage.py migrate

# Create the models class with their fields
# edit app/models.py

# Plug app into project
python3 manage.py makemigrations polls

# To see SQL that generate the created model
python3 manage.py sqlmigrate polls 0001

# Check problems in the projects
python3 manage.py check

# Create the models in the db
python3 manage.py migrate

# Change your models (in models.py).
# Run python manage.py makemigrations to create migrations for those changes
# Run python manage.py migrate to apply those changes to the database.

# Run Django Shell
python3 manage.py shell

# Import models
from polls.models import Choice, Question

# Requests
Question.objects.all() # Need to add __str__ method.
from django.utils import timezone
q = Question(question_text="What's new?", pub_date=timezone.now())

# Save object in db
q.save()
q.id
q.question_text
q.pub_date

# Change value and save
q.question_text = "What's up?"
q.save()
q.question_text

# Filters
Question.objects.filter(id=1)
Question.objects.filter(question_text__startswith='What')

# Timezone
from django.utils import timezone
current_year = timezone.now().year
Question.objects.get(pub_date__year=current_year)

# Use a model method
# Add method was_published_recently() in a Model in models.py
# Run the shell again
from polls.models import Choice, Question
q = Question.objects.get(pk=1)
q.was_published_recently()

# Create an admin
python3 manage.py createsuperuser
http://127.0.0.1:8000/admin

# Add an admin interface to app
# In app/admin.py
from .models import Question
admin.site.register(Question)
python3 manage.py runserver
http://127.0.0.1:8000/admin

