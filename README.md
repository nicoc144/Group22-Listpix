Django Documentation: https://docs.djangoproject.com/en/5.1/

How to Build:
(Preffered IDE: VS Code)

1. Clone the project and pull the code from the repository.
2. Make sure you have django and bootstrap installed "pip3 install django" and "pip install django-bootstrap-v5"
3. In the "Group22-Listpix" file type the command "source listpixenv/bin/activate" to activate the virtual environment.
4. Change directory to the "listpixProj" file.
5. Type the command "python manage.py runserver" to run the server (it should produce a link which will link you to the user's view).

How to navigate to the admin page:
1. You can create an admin account using the command "python manage.py createsuperuser" in terminal.
2. You can go to the admin page by adding "/admin" to the url.

How to migrate to the database:
1. Type command "python manage.py makemigrations" to generate migration files from the models to the database (database handling is done automatically by django via this command)
2. Type command "python manage.py migrate" to actually apply the changes to the database

Future Features:
1. Security - Account Lockout
2. List Generation/Management - Reroll ability
3. Interactions - Users can follow other users

Additional Resources Used:
https://www.geeksforgeeks.org/create-social-media-feed-app-using-django/ 
