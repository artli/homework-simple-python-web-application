from bottle import Bottle, run, static_file, view


app = Bottle()


@app.get('/')
@view('index')
def show_index():
    return {}


@app.post('/')
def perform_action():
    return 'Add or delete a link and redirect to main page'


@app.get('/<link_id:re:[^-/]+>')
def follow_link(link_id):
    return 'Redirect to wherever link "{}" points'.format(link_id)


@app.get('/<link_id:re:[^-/]+->')
@view('stat')
def show_link_stat(link_id):
    return {'link_id': link_id}


@app.get('/static/<filepath:path>')
def send_static_file(filepath):
    return static_file(filepath, '/static')


run(app, host='localhost', port=8080, debug=True)