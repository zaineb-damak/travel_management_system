# travel_management_system

This project is a web application for managing bookings for travel packages. Users can view available travel packages, make bookings and make fake payments.

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/zaineb-damak/travel_management_system.git
    $ cd travel_management_system
    
Activate the virtualenv for your project.

    $ python -m venv venv
    $ source venv/bin/activate
    
Install project dependencies:

    $ pip install -r requirements.txt
    
Then apply the migrations:

    $ python manage.py migrate
    
Create a superuser for testing: 
    
    $ python manage.py createsuperuser

You can now run the development server:

    $ python manage.py runserver

Start RabbitMQ server:

    $ rabbitmq-server

Start the Celery worker:

    $ celery -A tms worker -l info

# Project Features

View available travel packages

Make bookings for selected packages

Make payments for bookings

Receive email confirmation after completing a payment

Download a PDF invoice after creating a booking

# Technologies Used

Django

Django REST Framework

SQLite

Celery

RabbitMQ: Message broker used for communication between Celery workers





