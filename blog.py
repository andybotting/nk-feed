import re
from datetime import datetime, timedelta
from google.appengine.api import urlfetch

import feedparser

feed_url = 'http://www.natkringoudis.com.au/feed/'

def entries(days=6):
    feedinput = urlfetch.fetch(feed_url)
    rss_parsed = feedparser.parse(feedinput.content)
    lastdays = datetime.now() - timedelta(days=days, seconds=0)

    # Get entries from days limit and convert from timestruct to datetime
    entries = [e for e in rss_parsed['entries']
               if datetime(*e.published_parsed[:6]) > lastdays]
    entries.sort(key=lambda p: p.published_parsed, reverse=True)

    for e in entries:
        # Remove the paragraph 'The post*'
        e['summary'] = re.sub(ur'<p>The post.*</a>.</p>', ur'', e['summary'])
        # Add a break after the image
        e['summary'] = re.sub(ur'(<img .*?>)', ur'<p>\1</p>', e['summary'])
        # Remove Continue link
        e['summary'] = re.sub(ur'(\s?<a href=".*">Continued</a>)', '', e['summary'])

    return entries
