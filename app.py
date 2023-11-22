import requests
from flask import Flask
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app, version='1.0', title='Simple Flask Application', description='A simple Flask App with Swagger. \
          Contains endpoints that read from dicts as well as APIs.')

# Create a parser to handle parameters
parser = reqparse.RequestParser()
parser.add_argument('topic', type=str, help='Topic to find favorites of')


FAVORITES = {
    "animal": "dog",
    "country": "Japan",
    "color": "blue",
    "food": "spaghetti",
    "movie": "Interstellar",
    "show": "House of the Dragon"
}


def get_random_joke():
    """Function for getting a random joke from the JokeAPI"""
    url = "https://v2.jokeapi.dev/joke/Any"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # Raise an exception for bad responses (4xx and 5xx)

        joke_data = response.json()

        if joke_data['type'] == 'single':
            joke = joke_data['joke']
        elif joke_data['type'] == 'twopart':
            joke = f"{joke_data['setup']} {joke_data['delivery']}"
        else:
            joke = "Unexpected joke format."

        return joke

    except requests.exceptions.RequestException as e:
        print(f"Error fetching joke: {e}")
        return None


@api.route('/hello')
class HelloWorld(Resource):
    """Class for API calls under route /hello"""

    def get(self):
        """Simple hello world GET request"""
        return {'message': 'World!'}


@api.route('/favorites')
@api.doc(params={'topic': f'Topic to find favorite of. Available options: {list(FAVORITES.keys())}'})
class Favorites(Resource):
    """Class for API calls under route /favorites"""

    def get(self):
        """Takes a topic and returns Kevin's favorite for topic"""

        # Parse the request parameters
        args = parser.parse_args()

        # Access the parsed parameters
        topic = args['topic']
        if topic in FAVORITES:
            return {'message': f"Kevin's Favorite {topic} is '{FAVORITES[topic]}'!"}

        return {'error': f"Topic '{topic}' is not valid. Please select one of: {list(FAVORITES.keys())}"}


@api.route('/joke')
class Joke(Resource):
    """Class for API calls under route /joke"""

    def get(self):
        """Fetches a random joke from JokeAPI"""

        random_joke = get_random_joke()

        if random_joke:
            return random_joke

        return {"error": "Failed to fetch a joke."}


if __name__ == '__main__':
    app.run(debug=True)
