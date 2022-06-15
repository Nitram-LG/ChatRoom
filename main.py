import os
import time
import utils
import database
from dotenv import load_dotenv
from flask import Flask, render_template, Response, request, redirect, url_for, session, make_response

app = Flask(__name__)

load_dotenv()
app.secret_key = os.getenv('SECRET_KEY')


@app.route('/')
def root():
    return redirect(url_for('home'), code=301)


@app.route('/home')
def home():
    if request.cookies.get('UUID') is None:
        resp = make_response(render_template('home.html'))
        resp.set_cookie('UUID', utils.get_uuid())
        return resp
    else:
        return render_template('home.html')


@app.route('/chat')
def chat():
    if request.cookies.get('UUID') is None:
        resp = make_response(render_template('chat.html'))
        resp.set_cookie('UUID', utils.get_uuid())
        return resp
    else:
        return render_template('chat.html')


@app.route('/code')
def code():
    if request.cookies.get('UUID') is None:
        resp = make_response(render_template('code.html'))
        resp.set_cookie('UUID', utils.get_uuid())
        return resp
    else:
        return render_template('code.html')


@app.route('/send', methods=['POST'])
def send():
    try:
        logged_in = True if session['username'] else False
    except KeyError:
        logged_in = False

    if logged_in:
        content = f"{session['username']} : "
    else:
        content = f"Anon{request.cookies.get('UUID')} : "

    content += request.data.decode()
    utils.send(content)
    return '', 200


@app.route('/register', methods=['POST'])
def register():
    received = request.data.decode().split("|")

    if not database.check_user_exist(received[0]):
        status = 0
        database.create_user(*received)
    else:
        status = 1

    return Response(str(status), content_type="text/plain", status=200)


@app.route('/login', methods=['POST'])
def login():
    received = request.data.decode().split("|")

    if database.check_if_valid(*received):
        status = 2
        infos = database.load_user_info(received[0])
        session['username'] = infos[0][1]
    else:
        status = 3

    return Response(str(status), content_type="text/plain", status=200)


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))


@app.route('/stream')
def stream():
    def eventStream():
        while True:
            yield f"data: {utils.get_server_update()}\n\n"
            time.sleep(0.5)

    return Response(eventStream(), mimetype="text/event-stream")


if __name__ == "__main__":
    app.run()
