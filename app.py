from flask import Flask, request, render_template
import youtube_dl

app = Flask(__name__)


@app.route('/api/upload', methods=['GET'])
def youtube_upload():
    return render_template('index.html')  # 返回模版界面


@app.route('/api/upload', methods=['POST'])
def form_youtube_upload():
    if request.method == 'POST':  # 判断请求方式
        url = request.form['url']  # 获取传入表单的数据
        return do_update(url)


def do_update(url):
    ydl = youtube_dl.YoutubeDL()
    video = ydl.extract_info(url, download=False)
    return video


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello')
def hello():
    return 'hello'


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
