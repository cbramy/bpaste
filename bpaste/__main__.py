#!python3

import sys
import argparse
from logging import debug
from pyperclip import copy

from bpaste.uploader import BPaster
from bpaste.languages import languages
from bpaste import __appname__, __version__
from bpaste.exceptions import InvalidExpiryError, LanguageNotFoundError, NoCodeError, CodeUploadError

# set up some default values
EXIT_NO_ERROR = 0
EXIT_FILE_NOT_FOUND = 100
EXIT_NO_NETWORK_CONNECTION = 200
EXIT_INVALID_ARGUMENT_EXPIRY = 300
EXIT_INVALID_ARGUMENT_LANGUAGE = 400
EXIT_NO_CODE_FOUND_ERROR = 500
EXIT_CODE_UPLOAD_ERROR = 600
EXIT_NO_COMMAND_PROVIDED = 700

def main(args=None):
    if args is None:
        args = sys.argv[1:]

    # define main program parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', help='displays the version of this program', action='store_true')
    subparsers = parser.add_subparsers(title='subcommands', dest='command')

    # define `upload` program parser
    upload_parser = subparsers.add_parser('upload', help='upload the provided file\'s content to http://www.bpaste.net')
    upload_parser.add_argument('file', help='full path to the file to be bpasted')
    upload_parser.add_argument('-l', '--lang', help='language of the code to be bpasted (default: python3)')
    upload_parser.add_argument('-e', '--expire', help='expiry period for the code snippet (default: 1 day)')

    # define `list` program parser
    list_parser = subparsers.add_parser('list', help='displays the list of supported languages')

    args = vars(parser.parse_args())

    if args.get('command') == 'list':
        for x in range(len(languages)):
            print(languages[x].ljust(25), end=' ')
            if (x % 5) == 0: print('\n', end='')

        return EXIT_NO_ERROR

    elif args.get('command') == 'upload':
        expire = args.get('expire', '1day')
        language = args.get('lang', 'python3')

        # tries to open the provided file and read its content
        try:
            with open(args.get('file'), mode='r') as file:
                code = file.read()

        except FileNotFoundError:
            print('file not found: {}'.format(args.get('file')), file=sys.stderr)
            return EXIT_FILE_NOT_FOUND

        # tentatively upload the code snippet to bpaste.net and handles errors
        try:
            service = BPaster(expiry=expire, language=language)
            copy(service.submit(code))
            print('url copied in clipboard.')

        except InvalidExpiryError as e:
            print('invalid expiry value:', e.expiry, file=sys.stderr)
            return EXIT_INVALID_ARGUMENT_EXPIRY

        except LanguageNotFoundError as e:
            print('language not supported:', e.language, file=sys.stderr)
            return EXIT_INVALID_ARGUMENT_LANGUAGE

        except NoCodeError:
            print('cannot upload empty code.', file=sys.stderr)
            return EXIT_NO_CODE_FOUND_ERROR

        except CodeUploadError as e:
            print('an error occured when uploading code to bpaste.net:', e.status, file=sys.stderr)
            debug(e.content)
            return EXIT_CODE_UPLOAD_ERROR

    elif args.get('version', False):
        print(__appname__, __version__)

    else:
        return EXIT_NO_COMMAND_PROVIDED

if __name__ == '__main__':
    exit(main() or 0)
