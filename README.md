# Canyons ACM - Django Site
A website for Canyons ACM built using Django framework

### dependencies
    ```
    pip install Django
    pip install django-bootstrap4
    pip install django-crispy-forms
    pip install Pillow
    ```

### initializing project
in a root project folder, run:

    `django-admin startproject [SITE_NAME]`
    
### adding apps
for new apps, move to the directory with 'manage.py' and use:

    `python manage.py startapp [APP_NAME]`
then add the app name to the 'INSTALLED_APPS' list in 'settings.py'. to create the database or to make updates when required, and run:

### initializing database
    ```
    python manage.py makemigrations [APP_NAME]
    python manage.py migrate
    ```

### development configuration
lastly, create an admin account for development testing using:

    `python manage.py createsuperuser`
    