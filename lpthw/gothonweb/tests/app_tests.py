from nose.tools import *
from bin.app import app
from tests.tools import assert_response

def test_index():
	#404 check
	resp = app.request("/")
	assert_response(resp, status="404")

	#test GET request
	resp = app.request("/hello")
	assert_response(resp)

	#form test
	resp = app.request("/hello", method="POST")
	assert_response(resp, contains="Nobody")

	#test expected values
	data = ['name': 'Mark', 'greet': 'Hola']
	resp = app.request("/hello", method = "POST", data=data)
	assert_response(resp, contains="Mark")