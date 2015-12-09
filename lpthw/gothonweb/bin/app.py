import web 

urls = (
	'/', 'index'
)

app = web.application(urls, globals())

render = web.template.render('templates/', base="layout")

class index:
	def GET(self):
		greeting = "hello world"
		return render.index(greeting = greeting)

if __name__ == "__main__":
	app.run()