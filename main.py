from __future__ import unicode_literals, print_function, generators, division
from bottle import route, run, template


@route('/hello/<name>')
def index(name):
    return template('<b>Hello {{name}}</b>!', name=name)


run(host='localhost', port=8080)