NK Feed for Google App Engine
=============================

This is a simple app to fetch a feed from NK's blog and Instagram account
and generate a curated RSS feed for MailChimp.


Instagram
---------
This uses the Instagram API to fetch the latest images. The token and client
code are not checked in with this source.

You need to create a new application (can keep it sandboxed!) and add NK's
Instagram user ID (6204130) to the list of users available from the sandbox.

To generate a new access token, follow this URL (replace __CLIENT_ID__ with the actual Client ID from https://www.instagram.com/developer/clients/manage/):
https://www.instagram.com/oauth/authorize/?client_id=__CLIENT_ID__&redirect_uri=http://nk-feed-001.appspot.com/pics&response_type=token

If you get `This request requires scope=public_content, but this access token is not authorized with this scope`, then you need to request access to that scope, using the following URL:
https://www.instagram.com/oauth/authorize/?client_id=__CLIENT_ID__&redirect_uri=http://nk-feed-001.appspot.com/pics&response_type=code&scope=public_content


Installation
------------
  * Clone this repo
  * Install Google App Engine SDK for Python

IMPORTANT: To avoid committing Instagram API key:
`git update-index --assume-unchanged auth.py`

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
