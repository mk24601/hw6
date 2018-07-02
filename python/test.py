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

#class Data(ndb.Model):
#    w1 = ndb.StringProperty()
#    w2 = ndb.StringProperty()
#    patatokukasi = ndb.StringProperty()
 #   date = ndb.DateTimeProperty(auto_now_add=True)

class MainPage1(BaseHandler):
    def get(self):
        self.response.write(u'レッツぱたとくかしー！')
        #data = Data.query().order(-Data.date).fetch(1)
        #values = { 'data':data }
        self.render('main.html')

    def post(self):
        w1 = self.request.get('w1')
        w2 = self.request.get('w2')
        if w1 is None or w2 is None:
            self.redirect('/')
        
        #user = Data()
        result = ""
        for i in range(min(len(w1),len(w2))):
            result+= w1[int(i)]
            result+= w2[int(i)]
        if len(w1) < len(w2):
            result += w2[len(w2)-len(w1)-1:len(w2)]
        elif len(w2) < len(w1):
            result += w1[len(w1)-len(w2)-1:len(w1)]

        #user.w1 = w1
        #user.w2 = w2
        #user.patatokukasi = result
        #user.put()

        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write(result)
        self.render('main.html')

#class MainPage(webapp2.RequestHandler):
#    def get(self):
#        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
#        self.response.write(u'こんにちは！')

app = webapp2.WSGIApplication([
    ('/', MainPage1),
], debug=True)
