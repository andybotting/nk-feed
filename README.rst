NK Feed for Google App Engine
=============================

Installation
------------

  * Clone this repo
  * Install Google App Engine SDK for Python

Run via the App Engine development web server
---------------------------------------------
dev_appserver.py .

Test in the browser
-------------------
http://localhost:8080/blog
http://localhost:8080/pics

Upload to Google App Engine
---------------------------
appcfg.py -A nk-feed-001 update .

See http://code.google.com/appengine/docs/python/gettingstarted/uploading.html
