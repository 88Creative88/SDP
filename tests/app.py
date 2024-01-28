from flask import Flask
from gpiozero import CPUTemperature
import psutil

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/cpu/temp')
def cpu_temp():
    cpu = CPUTemperature()
    print(cpu)
    return f"{cpu.temperature}"

    #return 'CPU Temper'

@app.route('/cpu/temp/error')
def cpu_temp_error():
    cpu = 20
   # cpu = CPUTemperature()
    #if cpu.temperature > 60:
    if cpu < 60:
       # print("too hot")
        return "too hot"
    else:
       # print("fine")
        return "fine"
    #return 'CPU Temperature Error'

@app.route('/disk/usage')
def disk_usage():
    usage = psutil.disk_usage('/')
    print(usage)
    return f"{usage.percent}"
    #return 'Disk Usage'


if __name__ == '__main__':
    app.run()
