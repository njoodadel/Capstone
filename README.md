# Casting Agency App
## Motivation for project
The motivation of this project is to get the Nanodegree for the Full-Stack developer from Udacity.

## Run locally
#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

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

##### Export Variables 
To export the variables run this command which inclides the needed tokens and the database URI:
```
source setup.sh
```

#### Run the Tests
To run the tests for the endpoints please run this commande:
```
python3 test_app.py
```

## Run from heroku server
```Please import the postman collection named My Capstone.postman_collection```
In the collection you can find the roles which are Casting Assistant, Casting Director and Executive Producer
for each role the endpoins already setup with a body sample.

#### GET /movies
No body required

#### POST /movies
An example of the required body
```
{
    "title":"movie1",
    "release_date":"2020"
}
```
NOTE: title is unique

#### DELETE /movies/<int:movie_id>
No body required

#### PATCH /movies/<int:movie_id>
```
{
    "title":"movie1",
    "release_date":"2020"
}
```
You can edit the title, the date or both.

#### GET /actors
No body required

#### POST /actors
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
No body required

#### PATCH /actors/<int:actor_id>
```
{
    "name":"actor1",
    "gender":"female",
    "age":"40"
}
```
You can edit the name, the gender, the age or all.
