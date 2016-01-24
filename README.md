## bpaste

#### Purpose

This tools aims at making life easier by allowing to upload code files directly
to http://www.bpaste.net for the chosen language and/or expiry date.

This program is provided as open source under the GNU GPL 3 License (see the
  [LICENSE.md](https://github.com/cbramy/bpaste/blob/master/LICENSE.md) file for complete details). Use at your own risk.

#### Usage

The program works provide two commands described below:
* `upload` is the main command and is used to upload the provided file using the following format:  

  `bpaste.py upload [-l LANGUAGE] [-e EXPIRY] FILE`  

  * `LANGUAGE` being one of the supported language (see `list` command)
  * `EXPIRY` being one of the following self-explanatory expiry options:  
    * `1day`
    * `1week`
    * `1month`
    * `never`

* `list` displays the list of all the languages supported by this tool for upload. The is pretty big, so expect a long output when using this command:  

  `bpaste.py list`

#### Dependencies
* Python 3.5.1
* [httplib2](https://github.com/jcgregorio/httplib2) (0.9.2)
* [pyperclip](https://github.com/asweigart/pyperclip) (1.5.26)

#### Author(s)

* Clement Bramy

#### Contributors
