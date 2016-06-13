NK Feed for Google App Engine
=============================

This is a simple app to fetch a feed from NK's blog and Instagram account
and generate a curated RSS feed for MailChimp.


Instagram
---------
This uses the Instagram API to fetch the latest images. The token and client
code are not checked in with this source.

To generate a code, you can use the `get_access_token.py` script included in
the code from https://github.com/facebookarchive/python-instagram .

You need to create a new application (can keep it sandboxed!) and add NK's
Instagram user ID (6204130) to the list of users available from the sandbox.


Installation
------------
  * Clone this repo
  * Install Google App Engine SDK for Python

Run via the App Engine development web server
---------------------------------------------
```
dev_appserver.py .
```

Test
----
```
curl http://localhost:8080/blog
curl http://localhost:8080/pics
```

Upload to Google App Engine
---------------------------
```
appcfg.py -A nk-feed-001 update .
```

See http://code.google.com/appengine/docs/python/gettingstarted/uploading.html
