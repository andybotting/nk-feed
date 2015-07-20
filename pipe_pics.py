from pipe2py import Context
from pipe2py.modules import *

def pipe_pics(context, _INPUT, conf=None, **kwargs):
    "Pipeline"
    if conf is None:
        conf = {}

    if context.describe_input:
        return []

    forever = pipeforever.pipe_forever(context, None, conf=None)

    sw_54 = pipefetch.pipe_fetch(context, forever, conf={u'URL': {u'type': u'url', u'value': u'http://widget.websta.me/rss/n/natkringoudis'}})
    sw_112 = pipereverse.pipe_reverse(context, sw_54, conf={})
    sw_119 = pipetail.pipe_tail(context, sw_112, conf={u'count': {u'type': u'number', u'value': u'4'}})
    sw_130 = pipereverse.pipe_reverse(context, sw_119, conf={})
    sw_144 = piperegex.pipe_regex(context, sw_130, conf={u'RULE': [{u'field': {u'type': u'text', u'value': u'image.url'}, u'singlelinematch': {u'type': u'text', u'value': u'2'}, u'match': {u'type': u'text', u'value': u's306x306'}, u'replace': {u'type': u'text', u'value': u's200x200'}}, {u'field': {u'type': u'text', u'value': u''}, u'match': {u'type': u'text', u'value': u''}, u'replace': {u'type': u'text', u'value': u''}}]})
    #sw_137 = pipecreaterss.pipe_createrss(context, sw_144, conf={u'mediaContentHeight': {u'type': u'text', u'value': u''}, u'mediaThumbURL': {u'type': u'text', u'value': u''}, u'mediaContentType': {u'type': u'text', u'value': u''}, u'description': {u'type': u'text', u'value': u'image.url'}, u'pubdate': {u'type': u'text', u'value': u''}, u'author': {u'type': u'text', u'value': u''}, u'title': {u'type': u'text', u'value': u''}, u'mediaThumbHeight': {u'type': u'text', u'value': u''}, u'link': {u'type': u'text', u'value': u''}, u'mediaContentWidth': {u'type': u'text', u'value': u''}, u'mediaContentURL': {u'type': u'text', u'value': u''}, u'guid': {u'type': u'text', u'value': u''}, u'mediaThumbWidth': {u'type': u'text', u'value': u''}})
    sw_137 = pipecreaterss.pipe_createrss(context, sw_144, conf={u'mediaContentHeight': {u'type': u'text', u'value': u''}, u'mediaThumbURL': {u'type': u'text', u'value': u''}, u'mediaContentType': {u'type': u'text', u'value': u''}, u'description': {u'type': u'text', u'value': u'image.url'}, u'pubdate': {u'type': u'text', u'value': u''}, u'author': {u'type': u'text', u'value': u''}, u'title': {u'type': u'text', u'value': u''}, u'mediaThumbHeight': {u'type': u'text', u'value': u''}, u'link': {u'type': u'text', u'value': u''}, u'mediaContentWidth': {u'type': u'text', u'value': u''}, u'mediaContentURL': {u'type': u'text', u'value': u''}, u'guid': {u'type': u'text', u'value': u'guid'}, u'mediaThumbWidth': {u'type': u'text', u'value': u''}})
    sw_334 = piperegex.pipe_regex(context, sw_137, conf={u'RULE': [{u'field': {u'type': u'text', u'value': u'description'}, u'singlelinematch': {u'type': u'text', u'value': u'2'}, u'match': {u'type': u'text', u'value': u'(.*)'}, u'replace': {u'type': u'text', u'value': u'<a href="https://instagram.com/natkringoudis/"><img width=200 height=200 src="$1"></a>'}}]})
    _OUTPUT = pipeoutput.pipe_output(context, sw_334, conf={})
    return _OUTPUT

if __name__ == "__main__":
    context = Context()
    p = pipe_pics(context, None)
    for i in p:
        print i

