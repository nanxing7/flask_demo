from flask import Flask, request
import youtube_dl
from concurrent.futures import ThreadPoolExecutor

executor = ThreadPoolExecutor(1)

app = Flask(__name__)


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
        executor.submit(do_update(url))
    return '2333'


def do_update(url):
    # with youtube_dl.YoutubeDL as ydl:
    #     video = ydl.extract_info(url, download=False)
    return '23333'


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello')
def hello():
    return 'hello'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
