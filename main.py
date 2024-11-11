from flask import Flask
from flask_cors import CORS
from functions import fetch_cities, fetch_colleges, fetch_courses, fetch_course

app = Flask(__name__)

CORS(app)

app.add_url_rule('/fetch_cities', 'fetch_cities', fetch_cities, methods=['GET'])
app.add_url_rule('/fetch_colleges/<uf>/<city>', 'fetch_colleges', fetch_colleges, methods=['GET'])
app.add_url_rule('/fetch_courses/<college>/<campus>', 'fetch_courses', fetch_courses, methods=['GET'])
app.add_url_rule('/fetch_course/<course_id>', 'fetch_course', fetch_course, methods=['GET'])


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
