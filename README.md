# Casting Agency App
This Casting Agency app is an example of an api for managing  movies and their actors.
This does not have a frontend implemented yet.

Heroku link
```
https://njood-capstone.herokuapp.com
```
## Motivation for project
The motivation of this project is to get the Nanodegree for the Full-Stack developer from Udacity.

## Run locally
#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
```
python -m venv venv
venv/bin/activate
```

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies
- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) and [Flask-SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/) are libraries to handle the lightweight sqlite database.
- [jose](https://python-jose.readthedocs.io/en/latest/) JavaScript Object Signing and Encryption for JWTs. Useful for encoding, decoding, and verifying JWTS.

#### Local Database Setup
Once you create the database, open your terminal, navigate to the root folder, and run:
```
flask db init
flask db migrate
flask db upgrade
```
After running, don't forget modify 'SQLALCHEMY_DATABASE_URI' variable.


##### Export Variables 
To export the variables run this command which inclides the needed tokens and the database URI:
```
source setup.sh
```

#### Local Testing

To test your local installation, run the following command from the root folder:
```
python3 test_app.py
```
If all tests pass, your local installation is set up correctly.

#### Running the server
```
export FLASK_APP=app.py
export FLASK_DEBUG=true
export FLASK_ENV=development
flask run
```
## Run from heroku server
```Please import the postman collection named My Capstone.postman_collection```
In the collection you can find the roles which are Casting Assistant, Casting Director and Executive Producer
for each role the endpoins already setup with a body sample.
#### Permissions
- ##### Casting Assistant
  - get:actors
  - get:movies
- ##### Casting Director
  - get:actors
  - get:movies
  - post:actors (add an actor)
  - patch:actors (edit an actor)
  - patch:movies (edit a movie)
  - delete:actors
- ##### Executive Producer
   - get:actors
  - get:movies
  - post:actors (add an actor)
  - post:movies (add a movie)
  - patch:actors (edit an actor)
  - patch:movies (edit a movie)
  - delete:actors
  - delete:movies
  
#### GET /movies
This endpoint returns a list of movies
No body required

#### POST /movies
This endpoint enables you to add a new movie
An example of the required body
```
{
    "title":"movie1",
    "release_date":"2020"
}
```
NOTE: title is unique

#### DELETE /movies/<int:movie_id>
This endpoint enables you to delete a movie

No body required

#### PATCH /movies/<int:movie_id>
This endpoint enables you to edit a movie

```
{
    "title":"movie1",
    "release_date":"2020"
}
```
You can edit the title, the date or both.

#### GET /actors
This endpoint returns a list of actors
No body required

#### POST /actors
This endpoint enables you to add a new actor
An example of the required body
```
{
    "name":"actor1",
    "gender":"female",
    "age":"40"
}
```
NOTE: name is unique

#### DELETE /actors/<int:actor_id>
This endpoint enables you to delete an actor
No body required

#### PATCH /actors/<int:actor_id>
This endpoint enables you to edit an actor
```
{
    "name":"actor1",
    "gender":"female",
    "age":"40"
}
```
You can edit the name, the gender, the age or all.




