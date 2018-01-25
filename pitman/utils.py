import bleach
import re
import requests

from html import unescape
from readability.readability import Document

from .exceptions import ParseError
from .settings import PITMAN_UA, PITMAN_LANGUAGE_CODE


def process_html(html):
    doc = Document(html)
    return {
        'content': doc.content(),
        'clean_html': doc.get_clean_html(),
        'short_title': doc.short_title(),
        'summary': html_to_text(doc.summary()),
        'title': doc.title()
    }


def user_agent(ua=None):
    if not ua:
        return PITMAN_UA
    return ua


def accept_language_code(code=None):
    if not code:
        code = PITMAN_LANGUAGE_CODE
    if code.startswith('en'):
        return code
    try:
        lang = code.split("-")[0]
        code = '%s,%s' % (code, lang)
    except IndexError:
        pass
    return '{};q=0.8,en-US;q=0.6,en;q=0.4'.format(code)


def fetch_url(url, ua=None, language_code=None, verify_ssl=False):
    headers = {
        'Accept-Language': accept_language_code(language_code),
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
        'Accept-Encoding': 'identity,deflate,compress,gzip',
        'User-Agent': user_agent(ua)
    }
    return requests.get(url, headers=headers, verify=verify_ssl)


def process_url(url, verify_ssl=False):
    response = fetch_url(url, verify_ssl=verify_ssl)
    if response.status_code != 200:
        raise ParseError(
            'Unable to fetch url "{}" status code: {}'.format(
                url, response.status_code
            )
        )
    return process_html(response.text)


def replace_punctation(text):
    text = text.replace('’', "'")
    text = text.replace('“', '"')
    text = text.replace('”', '"')
    text = text.replace('–', '')
    text = text.replace('[', '')
    text = text.replace(']', '')
    return text


def clean_text(text):
    text = unescape(text)
    text = replace_punctation(text)
    text = re.sub(r'\n\s*\n', '\n\n', text)
    return text


def html_to_text(html):
    text = bleach.clean(html, tags=[], attributes={}, styles=[], strip=True)
    return clean_text(text)
