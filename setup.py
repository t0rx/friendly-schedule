
"""A setuptools based setup module.
See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path, read

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
  name = 'friendlyschedule',
  packages = ['friendlyschedule'],
  version = '0.4',
  description = 'Library for parsing human-friendly schedule strings',
  long_description = long_description,
  long_description_content_type='text/markdown',
  author = 't0rx',
  author_email = 't0rxon@googlemail.com',
  url = 'https://github.com/t0rx/friendly-schedule',
  download_url = 'https://github.com/t0rx/friendly-schedule/archive/0.4.tar.gz',
  keywords = ['schedule'],
  classifiers = [
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3.5',
    ],
)

