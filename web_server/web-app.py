import tornado.ioloop
import tornado.web
import os
class TtsHandler(tornado.web.RequestHandler):
    def get(self):
        text = self.get_argument("text", default=None, strip=False)
        print(text)
        cmd_str = '../bin/tts_exec '+text
        os.system(cmd_str)
        self.set_header ('Content-Type', 'application/octet-stream')
        self.set_header ('Content-Disposition', 'attachment; filename=a.wav')
        with open('./tts.wav', 'rb') as f:
            while True:
                data = f.read(64)
                if not data:
                    break
                self.write(data)
        self.finish()

application = tornado.web.Application([
    (r"/tts", TtsHandler),
    #(r'/a.wav', tornado.web.StaticFileHandler, {'path': './a.wav'}),
    (r'/tts.wav', TtsHandler),
])

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
