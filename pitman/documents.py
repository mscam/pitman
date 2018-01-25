from cached_property import cached_property
from textblob import TextBlob as tb
from .utils import process_html, process_url
from url_normalize import url_normalize
from .settings import PITMAN_VERIFY_SSL


class Document:
    def __init__(self, input):
        self._data = self.load(input)

    @staticmethod
    def load(input):
        if input.startswith('http'):
            url = url_normalize(input)
            data = process_url(input, verify_ssl=PITMAN_VERIFY_SSL)
        else:
            url = None
            data = process_html(input)
        data['url'] = url
        return data

    @classmethod
    def from_file(cls, input_file):
        if hasattr(input_file, 'read'):
            input = input_file.read()
        else:
            with open(input_file, 'r') as fd:
                input = fd.read()
        return cls(input)

    def _get_url(self):
        return self._data.get('url', '')

    def _set_url(self, value):
        self._data['url'] = url_normalize(value)

    url = property(_get_url, _set_url)

    @property
    def title(self):
        return self._data.get('title', '')

    @property
    def short_title(self):
        return self._data.get('short_title', '')

    @property
    def summary(self):
        return self._data.get('summary', '')

    @cached_property
    def blob(self):
        text = self.summary
        return tb(text)

    @cached_property
    def noun_phrases(self):
        return set([phrase for phrase in self.blob.noun_phrases])

    @cached_property
    def language(self):
        return self.blob.detect_language()

    def translate(self, to):
        return self.blob.translate(self.language, to=to)
