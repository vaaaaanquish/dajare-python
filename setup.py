from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

install_requires = ['beautifulsoup4', 'requests', 'requests-cache', 'tqdm']

setup(
    name='dajare',
    version='0.0.1',
    description='dajare search',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/vaaaaanquish/dajare-python',
    license='MIT',
    author='vaaaaanquish',
    author_email='6syun9@gmail.com',
    install_requires=install_requires,
    packages=['dajare'],
    package_dir={'dajare': 'dajare'},
    package_data={'dajare': ['dajare/*']},
    entry_points={"console_scripts": ["dajare = dajare.dajare_search:main"]},
    platforms='any',
)
