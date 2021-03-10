# NataCalc
# GAE application for calculating mean pace swimming times.


import webapp2
from webapp2_extras import jinja2

from core.libnatacalc import Calculator


def parse_float(s):
	toret = 0.0

	s = s.replace(',', '.')
	try:
		toret = float(s)
	except:
		toret = 0.0

	return toret


def parse_int(s):
	toret = 0

	try:
		toret = int(s)
	except:
		toret = 0

	return toret


class ResultsPage(webapp2.RequestHandler):
	AnswerPageFile = "answer.html"

	def load_input(self):
		return (parse_int(self.request.get("h", "0")),
				parse_int(self.request.get("m", "1")),
				parse_int(self.request.get("s", "30")),
				parse_float(self.request.get("d", "0.1")))

	def post(self):
		hours, minutes, seconds, distance = self.load_input()
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

		jinja = jinja2.get_jinja2(app=self.app)
		self.response.write(jinja.render_template(ResultsPage.AnswerPageFile, **template_values))


app = webapp2.WSGIApplication([
	('/calc', ResultsPage),
], debug=True)
