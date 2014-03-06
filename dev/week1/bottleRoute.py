import bottle

@bottle.route('/')
def home_page():
	return "Hello, World"

@bottle.route('/testpage')
def test_page():
	return "Test"

bottle.debug(True)
bottle.run(host='localhost', port=8080)
