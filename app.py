import tornado.ioloop
import tornado.web
import json
import talon
from talon import quotations
from tornado.options import define, options

class MainHandler(tornado.web.RequestHandler):
    def post(self):
    	json_response = {}
    	input_data = self.request.body
    	try:
    		input_data = json.loads(input_data)
    		data_type = input_data["type"]
    		content = input_data["content"]
    		reply = quotations.extract_from(content, data_type)
    		json_response["Success"]=True
    		#json_response["content"]=reply
    		json_response["position"]=len(reply)-1
    		self.write(json_response)
        except Exception,e:
        	print e
        	json_response["Success"] = False
        	self.write(json_response)

    def get(self):
        json_response = {}
        json_response["Success"] = True
        self.write(json_response)


def make_app():
    return tornado.web.Application([
        (r"/api/v1/mail/parser/", MainHandler),
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    define("port", default="8080", help="Port")
    tornado.options.parse_command_line()
    app = make_app()
    app.listen(options.port)
    tornado.ioloop.IOLoop.current().start()