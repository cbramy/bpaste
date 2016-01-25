from os import path
from codecs import open
from bpaste import __appname__, __version__
from setuptools import setup, find_packages

setup(
    name = __appname__,
    version = __version__,
    description = 'Code snippet uploader for bpaste.net',
    long_description = 'This tools can be used to upload files of code to https://bpaste.net',
    url = 'https://github.com/cbramy/bpaste',

    author = 'Clement Bramy',
    author_email = 'clement.bramy@gmail.com',

    license = 'GPLv3',
    keywords = 'code snippet bpaste syntax',

    packages = ['bpaste'],
    install_requires = [
        'httplib2>=0.9.2',
        'pyperclip>=1.5.26'
    ],

    entry_points = {
        'console_scripts': [
            'bpaste = bpaste.__main__:main'
        ]
    },


    classifiers = [
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Other Audience',
        'Intended Audience :: System Administrators',

        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.0',
        'Programming Language :: Python :: 3.1',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',

        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Environment :: Console',

        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Communications :: File Sharing',
        'Topic :: Software Development',
        'Topic :: Terminals',
        'Topic :: Text Editors',
        'Topic :: Text Processing',
        'Topic :: Utilities'
    ]
)
