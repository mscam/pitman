#!/usr/bin/env python3

import sys
import argparse
import json
from urllib.parse import urlparse
import pitman


def main():
    parser = argparse.ArgumentParser(description='Fetch text data from urls.')
    parser.add_argument('--limit', type=int, default=None,
                        help='Limit summary text to "n" chars.')
    parser.add_argument('--noun-phrases', default=False, action='store_true',
                        help='Extract noun phrases from text.')
    parser.add_argument('url')
    args = parser.parse_args()
    parsed = urlparse(args.url)
    if not parsed.scheme or not parsed.netloc:
        sys.stderr.write('The provided url is not valid!\n')
        return

    doc = pitman.Document(args.url)
    data = {
        'title': doc.title,
        'short_title': doc.short_title,
        'summary': doc.summary if not args.limit else doc.summary[:args.limit],
    }
    if args.noun_phrases:
        data['noun_phrases'] = list(doc.noun_phrases)

    sys.stdout.write(json.dumps(data, sort_keys=False, indent=4))


if __name__ == '__main__':
    main()
