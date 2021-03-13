import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from models import setup_db, Actors, Movies, db
from auth import AuthError, requires_auth


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    CORS(app)
    setup_db(app)

    @app.route('/check')
    def method_name():
        print("ping")
        return ""

# Movies
    # Get Movies
    @app.route('/movies', methods=["GET"])
    @requires_auth('get:movies')
    def get_movies(payload):
        moviesList = []
        movies = Movies.query.all()

        for movie in movies:
            moviesList.append(movie.format())

        if len(moviesList) == 0:
            abort(404)

        return jsonify({"success": True, "movies": moviesList})

    # Add new Movie
    @app.route('/movies', methods=["POST"])
    @requires_auth('post:movie')
    def add_movie(payload):
        body = request.get_json()
        new_title = body.get('title', None)
        new_release_date = body.get('release_date', None)

        if new_title is None or new_release_date is None:
            abort(422)

        try:
            movie = Movies(title=new_title, release_date=new_release_date)
            movie.insert()
        except BaseException:
            abort(422)

        return jsonify({
            'success': True,
            'id': movie.id,
        })

    # Delete a Movie
    @app.route('/movies/<int:movie_id>', methods=["DELETE"])
    @requires_auth('delete:movie')
    def delete_movie(payload, movie_id):
        movie = Movies.query.filter(Movies.id == movie_id).one_or_none()
        if movie is None:
            abort(404)

        movie.delete()
        return jsonify({
            "success": True,
            "deleted": movie.id,
        })

    # Edit a Movie
    @app.route('/movies/<int:movie_id>', methods=["PATCH"])
    @requires_auth('patch:movie')
    def edit_movie(payload, movie_id):
        body = request.get_json()
        print(body, "::::::::")
        if body is None:
            abort(422)

        movie = Movies.query.filter(Movies.id == movie_id).one_or_none()

        if movie is None:
            abort(404)

        if 'title' in body:
            movie.name = body['title']

        if 'release_date' in body:
            movie.release_date = body['release_date']

        movie.update()
        return jsonify({
            'success': True,
            'movie': movie.format()
        })

#---------------------------------------#

# Actors
    # Get Actors
    @app.route('/actors', methods=["GET"])
    @requires_auth('get:actors')
    def get_actors(payload):
        actorList = []
        actors = Actors.query.all()

        for actor in actors:
            actorList.append(actor.format())

        if len(actorList) == 0:
            abort(404)

        return jsonify({"success": True, "actors": actorList})

    # Add new Actor
    @app.route('/actors', methods=["POST"])
    @requires_auth('post:actor')
    def add_actor(payload):
        body = request.get_json()
        new_name = body.get('name', None)
        new_gender = body.get('gender', None)
        new_age = body.get('age', None)

        if new_name is None or new_gender is None or new_gender is None:
            abort(422)

        try:
            actor = Actors(name=new_name, gender=new_gender, age=new_age)
            actor.insert()
        except BaseException:
            abort(422)

        return jsonify({
            'success': True,
            'id': actor.id,
        })

    # Delete an Actor
    @app.route('/actors/<int:actor_id>', methods=["DELETE"])
    @requires_auth('delete:actor')
    def delete_actor(payload, actor_id):
        actor = Actors.query.filter(Actors.id == actor_id).one_or_none()

        if actor is None:
            abort(404)

        actor.delete()
        return jsonify({
            "success": True,
            "deleted": actor.id,
        })

    # Edit an Actor
    @app.route('/actors/<int:actor_id>', methods=["PATCH"])
    @requires_auth('patch:actor')
    def edit_actor(payload, actor_id):
        body = request.get_json()
        print(body, "::::::::")
        if body is None:
            abort(422)

        actor = Actors.query.filter(Actors.id == actor_id).one_or_none()

        if actor is None:
            abort(404)

        if 'name' in body:
            actor.name = body['name']

        if 'gender' in body:
            actor.gender = body['gender']

        if 'age' in body:
            actor.age = body['age']

        actor.update()
        return jsonify({
            'success': True,
            'actor': actor.format()
        })


# Error handling

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad Request"
        })

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Not found"
        })

    @app.errorhandler(422)
    def unprocessable_entity(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable Entity"
        })

    @app.errorhandler(500)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal Server Error"
        })

    @app.errorhandler(422)
    def server_error(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Missing Permissions"
        })

    return app


app = create_app()


if __name__ == '__main__':
    app.run(host='https://njood-capstone.herokuapp.com', port=8080, debug=True)
