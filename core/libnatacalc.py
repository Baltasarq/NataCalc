# libnatacalc.py


class Calculator:
	def __init__(self, d, h, m, s):
		self.distance = float(d)
		self.hours = float(h)
		self.minutes = float(m)
		self.seconds = float(s)

		self.kmsh = 0.0
		self.t100m = 0.0
		self.t1000m = 0.0

	@staticmethod
	def cnvt_to_seconds(h, m, s):
		return s + (m * 60) + (h * 3600)

	@staticmethod
	def format_time(v):
		toret = ""

		h = v / 3600
		m = (v % 3600) / 60
		s = (v % 3600) % 60

		strH = "%02d" % h
		strM = "%02d" % m
		strS = "%02d" % s

		toret = strH + "h " + strM + "' " + strS + "\""
		return toret

	def calculate(self):
		total = Calculator.cnvt_to_seconds(self.hours, self.minutes, self.seconds)

		total = float( total )

		if (total > 0
		and self.distance > 0):
			# Results
			self.kmsh = self.distance / (total / 3600.0)
			self.t1000m = total / self.distance
			self.t100m = total / (self.distance * 10.0)

	def get_kms_per_hour(self):
		return self.kmsh

	def get_time_per_100m(self):
		return self.t100m

	def get_time_per_1000m(self):
		return self.t1000m

	def get_distance(self):
		return self.distance

	def get_time(self):
		return self.hours, self.minutes, self.seconds
