import flask 

app = flask.Flask(__name__)

@app.route('/')
def index():
    return 'Hello World'

@app.route('/about')
def about():
    return 'About Page'

if __name__ == '__main__':
    app.run(debug=False)    