try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setuptools

config = {
    'description': 'Code for Exercise 47 in LPHW',
    'author': 'Keshav Mahindra',
    'url': '',
    'download_url': '',
    'author_email': 'keshavmahindra@gmail.com',
    'version': '0.1',
    'install_requires': ['nose']
    'packages': ['ex47'],
    'scripts': [],
    'name': 'ex47 code'
}

setup(**config)
