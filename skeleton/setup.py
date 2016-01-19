try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Demo Project',
    'author': 'Tushar',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'tushar.mate@cuelogic.co.in',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
