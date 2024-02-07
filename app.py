#! /bin/env python
# NataCalc (c) 2022 Baltasar MIT License <jbgarcia@uvigo.es>
# Application for calculating mean pace swimming times.


import flask
from core.libnatacalc import Calculator


app = flask.Flask(__name__)


def parse_float(s):
    toret = 0.0

    if s:
        s = s.replace(',', '.')
        try:
            toret = float(s)
        except:
            toret = 0.0

    return toret


def parse_int(s):
    toret = 0

    if s:
        try:
            toret = int(s)
        except:
            toret = 0

    return toret


@app.route("/favicon.ico")
def get_static():
    return send_from_directory(app.static_folder, flask.request.path[1:])
    
    
def load_input():
    return (parse_int(flask.request.form.get("h", "0")),
            parse_int(flask.request.form.get("m", "1")),
            parse_int(flask.request.form.get("s", "30")),
            parse_float(flask.request.form.get("d", "0.1")))
            
    
@app.route("/calc", methods=["POST"])
def get_calc():
    hours, minutes, seconds, distance = load_input()
    calc = Calculator(distance, hours, minutes, seconds)
    calc.calculate()

    template_values = {
        'd': distance,
        'h': str.format("{:02d}", hours),
        'm': str.format("{:02d}", minutes),
        's': str.format("{:02d}", seconds),
        'kmsh': str.format("{:6.2f}", calc.get_kms_per_hour()),
        't100m': Calculator.format_time(calc.get_time_per_100m()),
        'tkm': Calculator.format_time(calc.get_time_per_1000m())
    }

    return flask.render_template("answer.html", **template_values)


@app.route("/")
def get_index():
    return flask.send_from_directory(app.static_folder, "index.html")
    
    
if __name__ == '__main__':
    app.run(port=5000, debug=True)
