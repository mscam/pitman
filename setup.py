import pip
from setuptools import setup, find_packages

# From https://gist.github.com/rochacbruno/90efe90e6549721e4189

links = []  # for repo urls (dependency_links)
requires = []  # for package names

# new versions of pip requires a session
requirements = pip.req.parse_requirements(
    'requirements.txt', session=pip.download.PipSession()
)

for item in requirements:
    if getattr(item, 'url', None):  # older pip has url
        links.append(str(item.url))
    if getattr(item, 'link', None):  # newer pip has link
        links.append(str(item.link))
    if item.req:
        requires.append(str(item.req))  # always the package name 


DESCRIPTION = ("Pitman is a small Python 3 library to extract text data from urls.")
LONG_DESCRIPTION = open('README.md').read()
VERSION = "0.1"


setup(
    name='pitman',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author='Massimo Scamarcia',
    author_email='massimo.scamarcia@gmail.com',
    url='http://github.com/mscam/pitman',
    license=open('LICENSE').read(),
    platforms=["any"],
    packages=find_packages(),
    install_requires=requires,
    dependency_links=links,
    include_package_data=True,
    test_suite="pitman.tests",
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
    ],
)
