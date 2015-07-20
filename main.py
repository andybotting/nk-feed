import webapp2
import logging
import cgi
import datetime
import time
import json
import os

from google.appengine.ext.webapp import template

from pipe2py import Context
from pipe_blog import pipe_blog
from pipe_pics import pipe_pics


class PipesEncoder(json.JSONEncoder): 
    """Extends JSONEncoder to add support for date and time properties. 
    """ 
    def default(self, obj): 
        """Tests the input object, obj, to encode as JSON.""" 
        if hasattr(obj, '__json__'): 
            return getattr(obj, '__json__')() 

        if isinstance(obj, datetime.datetime): 
            output = obj.strftime("%Y-%m-%dT%H:%M:%SZ")
            return output   
        elif isinstance(obj, time.struct_time): 
            dt = datetime.datetime.fromtimestamp(time.mktime(obj))
            output = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
            return output
  
        return json.JSONEncoder.default(self, obj)

class Blog(webapp2.RequestHandler):
    def get(self):
        self.response.headers["Content-Type"] = "application/json"
        params = dict([(arg, self.request.get(arg)) for arg in self.request.arguments()])
        context = Context(console=False, inputs=params)
        
        p = pipe_blog(context, None)
        entries = [e for e in p]

        dates = [datetime.datetime.strptime(str.join(' ', e.updated.split(None)[1:5]), "%d %b %Y %H:%M:%S") for e in entries]
        dates.sort(reverse=True)
        pub_date = dates[0].strftime("%a, %d %b %Y %H:%M:%S +0000")

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
        self.response.headers["Content-Type"] = "application/json"
        params = dict([(arg, self.request.get(arg)) for arg in self.request.arguments()])
        context = Context(console=False, inputs=params)

        p = pipe_pics(context, None)
        entries = [e for e in p].reverse()
        print(entries)
        pub_date = datetime.datetime.now().strftime("%a, %d %b %Y %H:%M:%S +0000")
        template_values = {'title': 'Nat Kringoudis', 
                           'description': 'Inspiring Wellness',
                           'feed_url': 'http://www.natkringoudis.com.au/feed/',
                           'pub_date': pub_date,
                           'posts': entries, 
                           'request': self.request}
        
        path = os.path.join(os.path.dirname(__file__), 'templates', 'pics.html')
        output = template.render(path, template_values)

        self.response.headers['Cache-Control'] = 'public,max-age=%s' % 86400
        self.response.headers['Content-Type'] = 'application/rss+xml'
        self.response.out.write(output)
        
app = webapp2.WSGIApplication([
    ('/blog', Blog),
    ('/pics', Pics)
], debug=True)

