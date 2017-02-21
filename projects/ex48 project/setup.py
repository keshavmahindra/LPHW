try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setuptools

config = {
    'description': 'Code for Exercise 48',
    'author': 'Keshav Mahindra',
    'url': '',
    'download_url': '',
    'author_email': 'keshavmahindra@gmail.com',
    'version': '0.1',
    'install_requires': ['nose']
    'packages': ['ex48'],
    'scripts': [],
    'name': 'ex48 project'
}

setup(**config)
