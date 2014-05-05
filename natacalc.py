#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os

import jinja2
import webapp2

from libnatacalc import Calculator

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader( os.path.dirname( __file__ ) ),
    extensions=[ "jinja2.ext.autoescape" ],
    autoescape=True )

def parseFloat(s):
	toret = 0.0;

	s = s.replace( ',', '.' );
	try:
		toret = float( s );
	except:
		toret = 0.0

	return toret;

def parseInt(s):
	toret = 0;

	try:
		toret = int( s );
	except:
		toret = 0

	return toret;

class ResultsPage(webapp2.RequestHandler):
	AnswerPageFile = "answer.html";

	def __init__(self, request=None, response=None):
		self.initialize( request, response )

		self.hours = parseInt( self.request.get( "h", "0" ) );
		self.minutes = parseInt( self.request.get( "m", "1" ) );
		self.seconds = parseInt( self.request.get( "s", "30" ) );
		self.distance = parseFloat( self.request.get( "d", "0.1" ) );

	def post(self):
		calc = Calculator( self.distance, self.hours, self.minutes, self.seconds );
		calc.calculate();

		template_values = {
			'd': self.distance,
			'h': str.format( "{0:02}", self.hours ),
			'm': str.format( "{0:02}", self.minutes ),
			's': str.format( "{0:02}", self.seconds ),
			'kmsh': str.format( "{0:4.2}", calc.getKmsPerHour() ),
			't100m': Calculator.formatTime( calc.getTimePer100m() ),
			'tkm': Calculator.formatTime( calc.getTimePer1000m() ),
                }

		template = JINJA_ENVIRONMENT.get_template( ResultsPage.AnswerPageFile )
		self.response.write( template.render( template_values ) );

app = webapp2.WSGIApplication([
    ('/calc', ResultsPage),
], debug=True)
