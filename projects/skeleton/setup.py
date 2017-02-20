try:
    from setuptools import setuptools
except ImportError:
    from distutils.core import setuptools

config = {
    'description': 'Skeleton Project',
    'author': 'Keshav Mahindra',
    'url': '',
    'download_url': '',
    'author_email': 'keshavmahindra@gmail.com',
    'version': '0.1',
    'install_requires': ['nose']
    'packages': ['NAME'],
    'scripts': [],
    'name': 'project name'
}

setup(**config)
