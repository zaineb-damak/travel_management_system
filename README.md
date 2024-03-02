# authentication-project

This Django project implements three different authentication methods for accessing API endpoints: JWT, API key, and user session.

# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/zaineb-damak/authentication-project.git
    $ cd authentication-project
    
Activate the virtualenv for your project.

    $ python -m venv venv
    $ source venv/bin/activate
    
Install project dependencies:

    $ pip install -r requirements.txt
    
Then simply apply the migrations:

    $ python manage.py migrate
    
Create a superuser for testing: 
    
    $ python manage.py createsuperuser

You can now run the development server:

    $ python manage.py runserver

# Project Structure

Models:

User: Inherits from AbstractUser and has fields - username, email, password, first_name, last_name, and api_key.

Post: Fields - title, content, author (foreign key to User), and created_at.

API Endpoints:

`/posts/`: GET request returns a list of all posts. JWT authentication.

`/posts/<id>/`: GET request returns a single post by id. API key authentication.

`/posts/create/`: POST request creates a new post. User session authentication.

`/users/`: GET request returns list of all users and POST request creates a new user

`/users/<id>/`: GET request returns a single user.

# Authentication

Use tools like Postman or curl to test the API endpoints with different authentication methods:

Obtain a JWT token: Send a POST request to `/api/token/` with your username and password.

Obtain an API key: Access the admin site at `/admin/` and create a new API key object for your user.



