# NataCalc (c) 2022 Baltasar MIT License <jbgarcia@uvigo.es>
# Application for calculating mean pace swimming times.


from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory

from core.libnatacalc import Calculator


app = Flask(__name__)


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


def load_input(request):
    return (parse_int(request.form["h"]),
            parse_int(request.form["m"]),
            parse_int(request.form["s"]),
            parse_float(request.form["d"]))


@app.route("/favicon.ico")
@app.route("/natacalc.css")
def get_static():
    return send_from_directory(app.static_folder, request.path[1:])


@app.route("/")
def get_index():
    return send_from_directory(app.template_folder, "index.html")


@app.route("/calc", methods=['POST'])
def post_calculate():
    hours, minutes, seconds, distance = load_input(request)
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

    return render_template("answer.html", **template_values)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
