from webob import Request, Response

class FrameWorkApp:
    def __call__(self, environ, start_response):
        req = Request(environ)
        res = self.handle_request(req)
        return res(environ, start_response)

    def handle_request(self,req ):
        print(req.environ)
        user_agent = req.environ.get("HTTP_USER_AGENT", "TOPILMADI")

        res = Response()
        res.text = f"Salom siz {user_agent} foydalanayabsan"
        return res



