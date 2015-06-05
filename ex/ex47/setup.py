try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'ex47',
    'author': 'bingoboy',
    'url': 'localhost',
    'download_url': 'localhost',
    'author_email': '827603830@qq.com',
    'version': '0.1',
    'install_require': ['nose'],
    'package': ['ex47'],
    'script': [],
    'name': 'ex47'
}

setup(**config)
