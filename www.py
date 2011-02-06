import tornado.httpserver
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write(getMainPage())

application = tornado.web.Application([
    (r"/", MainHandler),
])


def getMainPage():
	s = ""
	s += getPageHeader()
	s += getMainPageBody()
	s += getPageFooter()
	return s


def getPageHeader():
	t = ""
	t += ""
	return t
	

def getMainPageBody():
	t = ""
	t += ""
	return t


def getPageFooter():
	t = ""
	t += ""
	return t




if __name__ == "__main__":
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
