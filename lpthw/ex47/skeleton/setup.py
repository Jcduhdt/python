try:
    from setuptools import setup
except ImportError:
    from sidtutils.core import setup

config = {
    'description':'My Project',
    'author':'Zhang xiong',
    'url':'URL to get it at',
    'download_url':'Where to download it',
    'author_email':'My email',
    'version':'0.1',
    'install_requires':['nose'],
    'packages':['NAME'],
    'scripts':[],
    'name':'projectname'
}

setup(**config)
