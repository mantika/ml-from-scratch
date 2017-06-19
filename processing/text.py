import re
import translitcodec  # NOQA
from collections import Counter


def to_lower(text):
    return text.lower()


def transliterate(text):
    return text.encode('transliterate')


def alphanum(text, r=re.compile(r'[\w]+', re.U)):
    return u' '.join(r.findall(text))


def tokenize_url(text, r=re.compile(r'(https?://|www\.)([a-z0-9-]+\.)+[a-z]{2,6}(/[\w/%?&-]*)?', re.I | re.U)):
    return r.sub(u'__URL__', text)


def remove_tags(text, r=re.compile(r'(\s*)[@#](\w+)\b')):
    return r.sub(r'\1\2', text)


class GramsCounter:

    def __init__(self):
        self._counter = Counter()

    def feed(self, text):
        self._counter.update(text.split())

    def to_indexes(self, limit=None):
        words = sorted(self._counter.iteritems(), key=lambda (k, v): (v, k), reverse=True)
        if limit:
            words = words[:limit]
        return {w: i for i, (w, _) in enumerate(words)}
