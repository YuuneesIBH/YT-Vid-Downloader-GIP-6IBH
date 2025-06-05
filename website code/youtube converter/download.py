#hier begint de code voor de variabele uit de main.js te lezen --> FLask
import json
from flask import redirect, request
from flask import Flask, render_template
from pytube import YouTube
from pytube.cli import on_progress
from pathlib import Path


app = Flask(__name__, template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/test', methods=['POST'])
def test():
    output = request.get_json()
    print(output)

    print(type(output))
    result = json.loads(output)

    print(result)
    print(type(result))

    return result

@app.route('/handle_data', methods=['POST', 'GET'])
def handle_data():

    downloads_path = str(Path.home() / "Downloads")
    projectdata = request.form['searchvalue']

    #hier begint de code voor de conversie van het YouTube filmpje

    url = projectdata

    yt = YouTube(url, on_progress_callback=on_progress)

    save_path = downloads_path

    video = yt.streams.get_highest_resolution()
    video.download(output_path=save_path)

    request.args.get(video)
    return render_template('thankyou.html')

@app.route('/handle_audiodata', methods=['POST', 'GET'])
def handle_audiodata():

    downloads_path = str(Path.home() / "Downloads")
    projectdata = request.form['searchvalue']

    #hier begint de code voor de conversie van het YouTube filmpje

    url = projectdata

    yt = YouTube(url, on_progress_callback=on_progress)

    save_path = downloads_path

    video = yt.streams.get_by_itag(250)
    video.download(output_path=save_path)

    request.args.get(video)
    return render_template('thankyou.html')

@app.route('/youtubetomp3', methods=['POST', 'GET'])
def youtubetomp3():
    return render_template('index copy.html')

@app.route('/youtubetomp4', methods=['POST', 'GET'])
def youtubetomp4():
    return render_template('index.html')

@app.route('/return_main', methods=['GET'])
def return_main():
    return render_template('index.html')
    
if __name__ == "__main__":
    app.run(debug=True, port=5010)



