#!/usr/bin/env python
import os
import jinja2
import webapp2
from Loto_stevila import lot_stevila

# Poiskusi vsako metodo posebej
# e.g.:
# print os.path.dirname(__file__)
#  da vidis kaj naredi,
# poglej tudi dokumentacijo
# https://docs.python.org/2/library/os.path.html
template_dir = os.path.join(os.path.dirname(__file__), "templates")
# Povej jinji kje lahko najete nase template
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

class BaseHandler(webapp2.RequestHandler):
    """Ta class nam poenostavi delo s templati.
    Definiramo nekaj metod ki nam bodo pomagale,
    predvsem da se ne ponavljamo in da ne pisemo
    vec vrstic ampak le eno - klicemo metodo.
    """
    def write(self, *args, **kwargs):
        # Uporabo *args in **kwargs si preberi na
        # http://stackoverflow.com/questions/3394835/args-and-kwargs
        # http://stackoverflow.com/questions/36901/what-does-double-star-and-star-do-for-python-parameters
        return self.response.out.write(*args, **kwargs)

    def render_str(self, template, **params):
        template = jinja_env.get_template(template)
        return template.render(params)

    def render(self, template, **kwargs):
        return self.write(self.render_str(template, **kwargs))

    def render_template(self, view_filename, params=None):
        # POZOR! None se vedno primerja z "is"!
        # http://stackoverflow.com/questions/14247373/python-none-comparison-should-i-use-is-or
        # http://stackoverflow.com/questions/3257919/is-none-vs-none
        if params is None:
            params = {}
        template = jinja_env.get_template(view_filename)
        return self.response.out.write(template.render(params))



class MainHandler(BaseHandler):
    """Nas MainHandler podeduje od BaseHandler-ja, kar pomeni, da lahko
    uporabimo metode definirane v parent-u (BaseHandler).
    Glej predavanje 13 - OOP"""

    def get(self):
        """Metoda, ki bo klicana, ko server - nasa aplikacija
        prejme GET zahtevo.
        """
        params = {"kkk": ""}

        return self.render_template("index.html", params=params)


class lotoHandler(BaseHandler):
    def get(self):
        params = {"lotostevilo": lot_stevila(8,1,39)}
        return self.render_template("loto.html", params=params)


app = webapp2.WSGIApplication([
    webapp2.Route('/', MainHandler),
    ('/loto', lotoHandler),
], debug=True)