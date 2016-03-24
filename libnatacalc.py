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
	def cnvtToSeconds(h, m, s):
		return (s + (m * 60) + (h * 3600));

	@staticmethod
	def formatTime(v):
		toret = "";

		h = v / 3600;
		m = (v % 3600) / 60;
		s = (v % 3600) % 60;

		strH = "%02d" % h;
		strM = "%02d" % m;
		strS = "%02d" % s;

		toret = strH + "h " + strM + "' " + strS + "\"";
		return toret;



	def calculate(self):
		total = Calculator.cnvtToSeconds( self.hours, self.minutes, self.seconds );

                total = float( total )

                if ( total > 0 \
                 and self.distance > 0 ):
                        # Results
                        self.kmsh = self.distance / ( total / 3600.0 );
                        self.t1000m = total / self.distance;
                        self.t100m = total / ( self.distance * 10.0 );

	def getKmsPerHour(self):
		return self.kmsh;

	def getTimePer100m(self):
		return self.t100m;

	def getTimePer1000m(self):
		return self.t1000m;

	def getDistance(self):
		return self.distance;

	def getTime(self):
		return self.hours, self.minutes, self.seconds;

