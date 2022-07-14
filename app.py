from flask import Flask
from flask.json import jsonify

from model import *

app = Flask(__name__)


@app.get('/all')
def get_all():
    return jsonify([person.to_json() for person in Person.select()])


@app.get('/age/<name>')
def get_age(name):
    response = Person.select().where(Person.name == name).get()
    if response:
        return jsonify(response.age)
    else:
        return jsonify({'error': True, 'message': f'Coundn\'t find a person called {name}'})


@app.get('/oldest')
def get_oldest():
    response = Person.select()
    min_birthday = min(person.birthday for person in response)
    oldests = Person.select().where( Person.birthday == min_birthday )
    return jsonify([oldest.to_json() for oldest in oldests])


@app.get('/newest')
def get_newest():
    response = Person.select()
    max_birthday = max(person.birthday for person in response)
    newests = Person.select().where( Person.birthday == max_birthday )
    return jsonify([newest.to_json() for newest in newests])


@app.post('/insert/<name>/<birthday>')
def post_person(name, birthday):
    birthday = list(map(int, birthday.split('-')))
    Person(name=name, birthday=date(*birthday)).save()
    return 'OK'


app.run(debug=True)
