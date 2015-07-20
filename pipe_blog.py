import datetime

from pipe2py import Context
from pipe2py.modules import *

def pipe_blog(context, _INPUT, conf=None, **kwargs):
    "Pipeline"
    if conf is None:
        conf = {}

    if context.describe_input:
        return []

    forever = pipeforever.pipe_forever(context, None, conf=None)

    days_ago = datetime.date.today() - datetime.timedelta(days=6)
    days_string = days_ago.strftime('%m/%d/%Y')

    sw_53 = pipefetch.pipe_fetch(context, forever, conf={u'URL': {u'type': u'url', u'value': u'http://www.natkringoudis.com.au/feed/'}})
    sw_104 = pipesort.pipe_sort(context, sw_53, conf={u'KEY': [{u'field': {u'type': u'text', u'value': u'pubDate'}, u'dir': {u'type': u'text', u'value': u'DESC'}}]})
    sw_93 = pipefilter.pipe_filter(context, sw_104, conf={u'COMBINE': {u'type': u'text', u'value': u'and'}, u'MODE': {u'type': u'text', u'value': u'permit'}, u'RULE': [{u'field': {u'type': u'text', u'value': u'pubDate'}, u'value': {u'type': u'text', u'value': days_string}, u'op': {u'type': u'text', u'value': u'after'}}]})
    sw_238 = piperegex.pipe_regex(context, sw_93, conf={u'RULE': [{u'field': {u'type': u'text', u'value': u'description'}, u'singlelinematch': {u'type': u'text', u'value': u'2'}, u'match': {u'type': u'text', u'value': u'<p>The post.*</a>.</p>'}, u'replace': {u'type': u'text', u'value': u''}}, {u'field': {u'type': u'text', u'value': u'description'}, u'singlelinematch': {u'type': u'text', u'value': u'2'}, u'match': {u'type': u'text', u'value': u'(<img .*?>)'}, u'replace': {u'type': u'text', u'value': u'$1<br />'}}]})
    sw_94 = piperename.pipe_rename(context, sw_238, conf={u'RULE': [{u'newval': {u'type': u'text', u'value': u'content:encoded'}, u'field': {u'type': u'text', u'value': u'description'}, u'op': {u'type': u'text', u'value': u'copy'}}]})
    _OUTPUT = pipeoutput.pipe_output(context, sw_94, conf={})
    return _OUTPUT

if __name__ == "__main__":
    context = Context()
    p = pipe_blog(context, None)
    for i in p:
        print i

