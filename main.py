from bottle import Bottle, run, static_file, view, request, redirect, HTTPError
from manager import Manager
from model import Link
from utils import generate_id


app = Bottle()
manager = Manager('links.db')


@app.get('/')
@view('index')
def show_index():
    return {'links': manager.get_all_links()}


@app.post('/action/add')
def add_link():
    link_url = request.forms.get('link_url')
    autodelete = request.forms.get('autodelete') == 'on'
    password = request.forms.get('password', '')
    if link_url:
        while True:
            id = generate_id()
            if manager.get_link_by_id(id) is None:
                break
        manager.save(Link(id, link_url, autodelete, password))
    redirect('/')


@app.post('/action/delete')
def delete_link():
    link_id = request.forms.get('link_id', '').strip()
    password = request.forms.get('password', '')
    link = manager.get_link_by_id(link_id)
    if link:
        if link.check_password(password):
            manager.delete(link)
    redirect('/')


@app.get('/<link_id:re:[^-/]+>')
def follow_link(link_id):
    link = manager.get_link_by_id(link_id)
    if not link:
        raise HTTPError(404, 'Link not found')
    if link.autodelete:
        manager.delete(link)
    else:
        link.visits += 1
        manager.save(link)
    redirect(link.url)


@app.get('/<link_id:re:[^-/]+->')
@view('stat')
def show_link_stat(link_id):
    link_id = link_id[:-1]
    link = manager.get_link_by_id(link_id)
    if not link:
        raise HTTPError(404, 'Link not found')
    return {'link': link}


@app.get('/static/<filepath:path>')
def send_static_file(filepath):
    return static_file(filepath, '/static')


run(app, host='localhost', port=8080, debug=True)