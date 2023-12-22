# descartes assessment

## install dependencies
Navigate to the directory of the project withint terminal and use the command below to install all dependencies
pip install -r .\requirements.txt

## run the server
python manage.py runserver
(server will run by default on port 8000)

## run the tests
python manage.py test

## API details
### CRUD operations available for the following
/authors/
/authors/:id/
/posts/
/posts/:id/

Django ORM models can be found under ./myapp/models.py
