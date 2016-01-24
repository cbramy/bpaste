#! /usr/bin/python

import sys
import argparse
from logging import debug
from pyperclip import copy

from utils.uploader import BPaster
from utils.languages import languages
import utils.exceptions as exceptions

# set up some default values
EXIT_NO_ERROR = 0
EXIT_FILE_NOT_FOUND = 100
EXIT_NO_NETWORK_CONNECTION = 200
EXIT_INVALID_ARGUMENT_EXPIRY = 300
EXIT_INVALID_ARGUMENT_LANGUAGE = 400
EXIT_NO_CODE_FOUND_ERROR = 500
EXIT_CODE_UPLOAD_ERROR = 600

# define main program parser
parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(title='subcommands', dest='command')

# define `upload` program parser
upload_parser = subparsers.add_parser('upload', help='upload the provided file\'s content to http://www.bpaste.net')
upload_parser.add_argument('file', help='full path to the file to be bpasted')
upload_parser.add_argument('-l', '--lang', help='language of the code to be bpasted (default: python3)')
upload_parser.add_argument('-e', '--expire', help='expiry period for the code snippet (default: 1 day)')

# define `list` program parser
list_parser = subparsers.add_parser('list', help='displays the list of supported languages')

args = parser.parse_args()

if args.command == 'list':
    for x in range(len(languages)):
        print(languages[x].ljust(25), end=' ')
        if (x % 5) == 0: print('\n', end='')

    exit(EXIT_NO_ERROR)

args.lang = args.lang if args.lang else 'python3'
args.expire = args.expire if args.expire else '1day'

# tries to open the provided file and read its content
try:
    with open(args.file, mode='r') as file:
        code = file.read()

except FileNotFoundError:
    print('file not found: {}'.format(args.file), file=sys.stderr)
    exit(EXIT_FILE_NOT_FOUND)

# tentatively upload the code snippet to bpaste.net and handles errors
try:
    service = BPaster(expiry=args.expire, language=args.lang)
    copy(service.submit(code))
    print('url copied in clipboard.')

except exceptions.InvalidExpiryError as e:
    print('invalid expiry value:', e.expiry, file=sys.stderr)
    exit(EXIT_INVALID_ARGUMENT_EXPIRY)

except exceptions.LanguageNotFoundError as e:
    print('language not supported:', e.language, file=sys.stderr)
    exit(EXIT_INVALID_ARGUMENT_LANGUAGE)

except exceptions.NoCodeError:
    print('cannot upload empty code.', file=sys.stderr)
    exit(EXIT_NO_CODE_FOUND_ERROR)

except exceptions.CodeUploadError as e:
    print('an error occured when uploading code to bpaste.net:', e.status, file=sys.stderr)
    debug(e.content)
    exit(EXIT_CODE_UPLOAD_ERROR)
