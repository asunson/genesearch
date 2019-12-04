This is a project to create a standalone app to query RNASeq Data

# Cheatsheet

A reference sheet for useful Django commands

*Model Migrations*

- `python manage.py makemigrations genesearch`
    - For when the model is modified.
- `python manage.py migrate genesearch`
    - Synchronize database state with current models
- `python manage.py loaddata <fixure_name>`
    - Load fixture data into database

*Testing*

- `python manage.py test genesearch.tests`
    - Run the testing suite.

*Starting the App*

- `python manage.py runserver`
    - Start the app.