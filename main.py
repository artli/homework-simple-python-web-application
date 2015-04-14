from bottle import Bottle, run, static_file


app = Bottle()


@app.get('/')
def show_index():
    return 'Main page; form for adding a link; list of all links'


@app.post('/')
def add_link():
    return 'Add a link and redirect to main page'


@app.get('/<link_id:re:[^-/]+>')
def follow_link(link_id):
    return 'Redirect to wherever link "{}" points'.format(link_id)


@app.get('/<link_id:re:[^-/]+->')
def show_link_stat(link_id):
    return 'Show stat for link "{}"'.format(link_id)


@app.get('/static/<filepath:path>')
def send_static_file(filepath):
    return static_file(filepath, '/static')


run(app, host='localhost', port=8080, debug=True)