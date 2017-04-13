import webapp2
import logging
import cgi
import datetime
import time
import json
import os

from google.appengine.ext.webapp import template

import pics
import blog


class Blog(webapp2.RequestHandler):
    def get(self):
        entries = blog.entries()
        pub_date = entries[0]['published']

        template_values = {'title': 'Nat Kringoudis',
                           'description': 'Inspiring Wellness',
                           'feed_url': 'http://www.natkringoudis.com.au/feed/',
                           'pub_date': pub_date,
                           'posts': entries,
                           'request': self.request}

        path = os.path.join(os.path.dirname(__file__), 'templates', 'posts.html')
        output = template.render(path, template_values)

        self.response.headers['Cache-Control'] = 'public,max-age=%s' % 86400
        self.response.headers['Content-Type'] = 'application/rss+xml'
        self.response.out.write(output)


class Pics(webapp2.RequestHandler):
    def get(self):

        try:
            entries = pics.pics()

            pub_date = datetime.datetime.now().strftime(
                "%a, %d %b %Y %H:%M:%S +0000")

            template_values = {
                'title': 'Nat Kringoudis',
                'description': 'Inspiring Wellness',
                'feed_url': 'http://www.natkringoudis.com.au/feed/',
                'pub_date': pub_date,
                'posts': entries,
                'request': self.request}

            path = os.path.join(os.path.dirname(__file__),
                'templates', 'pics.html')
            output = template.render(path, template_values)

            self.response.headers['Cache-Control'] = 'public,max-age=86400'
            self.response.headers['Content-Type'] = 'application/rss+xml'
            self.response.out.write(output)
        except Exception as e:
            path = os.path.join(os.path.dirname(__file__),
                'templates', 'error.html')
            output = template.render(path, {'error': e})
            self.response.out.write(output)


app = webapp2.WSGIApplication([
    ('/blog', Blog),
    ('/pics', Pics)
], debug=True)

