import webapp2
import cgi

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "text/html"
        self.response.write("""
          <html>

<style>
  body, html {
  height: 100%;
}
* {
  box-sizing: border-box;
}

p {
font-size: x-large;

color: #F8F8FF
}
.bg-img {

  /* The image used */
  background-image: url("https://christinawehner.files.wordpress.com/2015/01/alien.jpg");
  /* Control the height of the image */
  min-height: 800px;
  /* Center and scale the image nicely */
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
  position: relative;
}
/* Add styles to the form container */
.container {
  position: absolute;
  margin: 20px;
  max-width: 300px;
  padding: 16px;
  background-color: white;
}
/* Full-width input fields */
  input[type=text], input[type=password] {
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  border: none;
  background: #f1f1f1;
}
input[type=text]:focus, input[type=password]:focus {
  background-color: #ddd;
  outline: none;
}
/* Set a style for the submit button */
.btn {
  background-color: #4CAF50;
  color: white;
  padding: 16px 20px;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;

</style>
  <head>
    <link rel="stylesheet" type="text/css" href="/static/style.css">
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
            <title>Ripley</title></head>
            <body>
               <div class="bg-img">

    <div>
            <p> Ripley? Is that you? </p>
              <form action="/welcome" method="post">
              <div id="userInput">
        <input id="textInput" type="text" name="my_name" placeholder="Your name please..." class="container">
      </div>
      </div>
              </form>
            </body>
            </html>""")


class Greeting(webapp2.RequestHandler):
    def post(self):
        username = cgi.escape(self.request.get("my_name"))
        if username == 'Ripley':
            welcome_string = """<html><body>
                            We are finally together, {}.
                            </body></html>""".format(username)
            self.response.headers["Content-Type"] = "text/html"
            self.response.write(welcome_string)
        else:
            welcome_string = """<html><body>
                             I don't know you, you say your name is {}? Do you 
                             know where Ripley is? I have waited so long.
                             </body></html>""".format(username)
            self.response.headers["Content-Type"] = "text/html"
            self.response.write(welcome_string)


routes = [('/', MainPage), ('/welcome', Greeting)]
my_app = webapp2.WSGIApplication(routes, debug=True)
