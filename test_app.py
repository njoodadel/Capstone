import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from app import create_app
from models import setup_db, Actors, Movies


class AgencyTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "agency"
        self.database_path = "postgres://{}/{}".format(
            'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.Executive_Producer_Token = os.environ['Executive_Producer_Token']
        self.Casting_Director_Token = os.environ['Casting_Director_Token']
        self.Casting_Assistant_Token = os.environ['Casting_Assistant_Token']

    def tearDown(self):
        """Executed after each test"""
        pass

    # /movies tests

    def test_valid_get_movies(self):
        response = self.client().get(
            '/movies',
            headers={
                "Authorization": "Bearer " +
                self.Casting_Assistant_Token})
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)

    def test_valid_post_movies(self):
        response = self.client().post(
            '/movies',
            headers={
                "Authorization": "Bearer " +
                self.Executive_Producer_Token},
            json={
                'title': 'movie102',
                'release_date': '2020'})
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)

    def test_invalid_post_movies(self):
        response = self.client().post(
            '/movies',
            headers={
                "Authorization": "Bearer " +
                self.Executive_Producer_Token},
            json={
                'release_date': '2020'})
        data = json.loads(response.data)
        self.assertEqual(data['success'], False)

    def test_valid_update_movies(self):

        new_movie = Movies(title='movie101', release_date='2020')
        new_movie.insert()
        movie_id = new_movie.id

        response = self.client().patch(
            f'/movies/{movie_id}',
            headers={
                "Authorization": "Bearer " +
                self.Executive_Producer_Token},
            json={
                'release_date': '2021'})
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)

    def test_invalid_update_movies(self):
        response = self.client().patch(
            '/movies/100',
            headers={
                "Authorization": "Bearer " +
                self.Executive_Producer_Token})
        data = json.loads(response.data)
        self.assertEqual(data['success'], False)

    def test_unauth_post_movies(self):
        response = self.client().post(
            '/movies',
            headers={
                "Authorization": "Bearer " +
                self.Casting_Assistant_Token},
            json={
                'title': 'movie102',
                'release_date': '2020'})
        data = json.loads(response.data)
        self.assertEqual(data['success'], False)

    def test_unauth_post_movies2(self):
        response = self.client().post(
            '/movies',
            headers={
                "Authorization": "Bearer " +
                self.Casting_Director_Token},
            json={
                'release_date': '2020'})
        data = json.loads(response.data)
        self.assertEqual(data['success'], False)


# /actors tests


    def test_valid_get_actors(self):
        response = self.client().get(
            '/actors',
            headers={
                "Authorization": "Bearer " +
                self.Casting_Assistant_Token})
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)

    def test_valid_post_actors(self):
        response = self.client().post(
            '/actors',
            headers={
                "Authorization": "Bearer " +
                self.Executive_Producer_Token},
            json={
                'name': 'actor101',
                'gender': 'male',
                "age": "23"})
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)

    def test_invalid_post_actors(self):
        response = self.client().post(
            '/actors',
            headers={
                "Authorization": "Bearer " +
                self.Executive_Producer_Token},
            json={})
        data = json.loads(response.data)
        self.assertEqual(data['success'], False)

    def test_valid_update_actors(self):

        new_actor = Actors(name="actor102", gender="male", age="23")
        new_actor.insert()
        actor_id = new_actor.id

        response = self.client().patch(
            f'/actors/{actor_id}',
            headers={
                "Authorization": "Bearer " +
                self.Executive_Producer_Token},
            json={
                'age': '24'})
        data = json.loads(response.data)
        self.assertEqual(data['success'], True)

    def test_invalid_update_actors(self):
        response = self.client().patch(
            '/actors/100',
            headers={
                "Authorization": "Bearer " +
                self.Executive_Producer_Token})
        data = json.loads(response.data)
        self.assertEqual(data['success'], False)

    def test_unauth_post_actor(self):
        response = self.client().post(
            '/movies',
            headers={
                "Authorization": "Bearer " +
                self.Casting_Assistant_Token},
            json={
                'title': 'movie102',
                'release_date': '2020'})
        data = json.loads(response.data)
        self.assertEqual(data['success'], False)


if __name__ == "__main__":
    unittest.main()
