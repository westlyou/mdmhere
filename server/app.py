# -*- coding: utf-8 -*-

from flask import Flask, send_from_directory
app = Flask(__name__,
            static_url_path='',
            static_folder='static')


@app.route("/")
def hello():
    return app.send_static_file('index.html')


@app.route("/enroll")
def enroll():
    resp = app.send_static_file('eyj.mobileconfig')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    resp.headers['Content-Type'] = 'application/x-apple-aspen-config;charset=utf-8'
    resp.headers['Content-Disposition'] = 'attachment;filename="mdm.mobileconfig"'
    return resp


@app.route('/static/<path:path>')
def send_js(path):
    print(path)
    return send_from_directory('static', path)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
