import os

__all__ = ('PITMAN_VERSION', 'PITMAN_UA', 'PITMAN_LANGUAGE_CODE', 'PITMAN_VERIFY_SSL')

PITMAN_VERSION = '0.1'
PITMAN_UA = os.environ.get('PITMAN_UA', 'Pitman/{}'.format(PITMAN_VERSION))
PITMAN_LANGUAGE_CODE = os.environ.get('PITMAN_LANGUAGE_CODE', 'en-US,en')
PITMAN_VERIFY_SSL = bool(int(os.environ.get('PITMAN_VERIFY_SSL', '0')))

