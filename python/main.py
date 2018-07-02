#!/usr/bin/env python
# -*- coding: utf-8 -*-

import webapp2
import os
import jinja2
from google.appengine.ext import ndb

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))

class MainPage(BaseHandler):
    def get(self):
        self.response.write(u'レッツパタトクカシー！')
        self.render('main.html')

    def post(self):
        w1 = self.request.get('w1')
        w2 = self.request.get('w2')
        if w1 is None or w2 is None:
            self.redirect('/')
        
        result = ""
        for i in range(min(len(w1),len(w2))):
            result+= w1[int(i)]
            result+= w2[int(i)]
        if len(w1) < len(w2):
            result += w2[len(w2)-len(w1)-1:len(w2)]
        elif len(w2) < len(w1):
            result += w1[len(w1)-len(w2)-1:len(w1)]

        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write(w1 + u' + ' + w2 + u' = ' + result)
        self.render('main.html')

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
