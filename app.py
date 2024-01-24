from flask import Flask
from flask import Blueprint




app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/cpu/temp')
def cpu_temp():
    return 'CPU Temper'

@app.route('/cpu/temp/error')
def cpu_temp_error():
    return 'CPU Temperature Error'

@app.route('/disk/usage')
def disk_usage():
    return 'Disk Usage'


def create_app():
    app = Flask(__name__)

    return app

if __name__ == '__main__':
    app.run()
