#!/usr/bin/env python
# -*- coding: utf-8 -*-　

# 私の作ったweb appは　https://stepweek6.appspot.com

import webapp2
import os
import jinja2
from google.appengine.ext import ndb

# http://blog.adamrocker.com/2014/08/beginning-google-appengine-python.html のコピペ
JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

#　http://blog.adamrocker.com/2014/08/beginning-google-appengine-python.html のコピペ
class BaseHandler(webapp2.RequestHandler):
    def render(self, html, values={}):
        template = JINJA_ENVIRONMENT.get_template(html)
        self.response.write(template.render(values))


class MainPage(BaseHandler):
    def get(self): # もし https://stepweek6.appspot.com に「GET」でアクセスがきたら(main.htmlの4行目の<form action="/" method="POST">ってやつ)これが走る
        self.response.write(u'レッツパタトクカシー！') # ページ上部に「レッツパタトクカシー！とだす」
        self.render('main.html') # その下にmain.htmlの内容を表示させる

    def post(self):# もし https://stepweek6.appspot.com に「POST」でアクセスがきたら(=誰かが二つの単語を入力して「submit」を押したら)これが走る
        w1 = self.request.get('w1') # main.htmlの5行目から取り出したw1の値をw1に代入(どっちも同じ名前の変数ですみません
        w2 = self.request.get('w2') # main.htmlの6行目から取り出したw2の値をw2に代入(どっちも同じ名前の変数ですみません
        if w1 is None or w2 is None: # もしw1もしくはw2が未入力だったら
            self.redirect('/') # https://stepweek6.appspot.com にジャンプする

        #############ここはパタトクカシーを生成している部分###########
        result = ""
        for i in range(min(len(w1),len(w2))):
            result+= w1[int(i)]
            result+= w2[int(i)]
        if len(w1) < len(w2):
            result += w2[len(w2)-len(w1)-1:len(w2)]
        elif len(w2) < len(w1):
            result += w1[len(w1)-len(w2)-1:len(w1)]
        #########################################################

        self.response.headers['Content-Type'] = 'text/html; charset=UTF-8'
        self.response.write(w1 + u' + ' + w2 + u' = ' + result) # 結果出力！

        self.render('main.html') # その下にmain.htmlの内容を表示させる

# 入力されたURLに対してどのclassを走らせるかを設定する部分(ルーティング)
app = webapp2.WSGIApplication([
    # https://stepweek6.appspot.comにアクセスした時に走るプログラムはこれ
    ('/', MainPage)

], debug=True)
