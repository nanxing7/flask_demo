from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello')
def hello():
    return 'hello'


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


def do_the_upload(url):
    return url


@app.route('/api/upload', methods=['GET'])
def youtube_upload():
    return '''<form action ="/api/upload" method = "post">
        <p><input name = "url"></p>
        <p><button type="submit">download to service</button></p>
        </form>'''


@app.route('/api/upload', methods=['POST'])
def form_youtube_upload():
    if request.method == 'POST':
        url = request.form['url']
        return url


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
