## bpaste

#### Purpose

This tools aims at making life easier by allowing to upload code files directly
to http://www.bpaste.net for the chosen language and/or expiry date.

This program is provided as open source under the GNU GPL 3 License (see the
  [LICENSE.md](https://github.com/cbramy/bpaste/blob/master/LICENSE.md) file for complete details). Use at your own risk.

#### Resources

* Official package: [PyPi](https://pypi.python.org/pypi/bpaste)
* Full documentation: [Read The Docs](https://bpaste.readthedocs.org/en/latest/)

#### Installation

``pip install bpaste``

#### Usage

The program works provide two commands described below:
* `upload` is the main command and is used to upload the provided file using the following format:  

  `bpaste.py upload [-l, --lang LANGUAGE] [-e, --expire EXPIRY] FILE`  

  * `LANGUAGE` being one of the supported language (see `list` command)
  * `EXPIRY` being one of the following self-explanatory expiry options:  
    * `1day`
    * `1week`
    * `1month`
    * `never`

* `list` displays the list of all the languages supported by this tool for upload. The is pretty big, so expect a long output when using this command:  

  `bpaste.py list`

#### Dependencies
* [Python](https://www.python.org/) (3.5.1)
* [Httplib2](https://github.com/jcgregorio/httplib2) (0.9.2)
* [Pyperclip](https://github.com/asweigart/pyperclip) (1.5.26)
* [Sphinx](http://www.sphinx-doc.org/) (1.3.5) -- to generate the documentation
* [Read The Docs Sphinx Theme](https://github.com/snide/sphinx_rtd_theme) (0.1.9)

#### Author(s)

* Clement Bramy

#### Contributors
