from urllib.parse import urlencode
from httplib2 import Http, ServerNotFoundError

from .languages import languages
from .exceptions import NoCodeError, InvalidExpiryError, CodeUploadError

class BPaster:
    http = Http()
    default2text = True
    default2oneday = True
    languages = languages
    expiries = ['1week', '1day', '1month', 'never']
    headers = {'cache-control': 'no-cache', 'content-type': 'application/x-www-form-urlencoded'}

    def __init__(self, url='https://bpaste.net/', expiry='1day', language='python3'):
        self.url = url
        self.__set_expiry(expiry)
        self.__set_lexer(language)

    def __set_expiry(self, expiry):
        if self.expiries.count(expiry) == 1: self.expiry = expiry
        elif self.default2oneday: self.expiry = '1day'
        else: raise InvalidExpiryError(expiry)

    def __set_lexer(self, language):
        if self.languages.count(language) == 1: self.lexer = language
        elif self.default2text: self.lexer = 'text'
        else: raise LanguageNotFoundError(language)

    def submit(self, code=None):
        if not code: raise NoCodeError()

        # post the form to bpaste.net
        body = urlencode(dict(code=code, lexer=self.lexer, expiry=self.expiry))

        try:
            response, content = self.http.request(self.url, 'POST', body=body, headers=self.headers)
        except ServerNotFoundError:
            raise CodeUploadError(-1, None)

        # check the response
        if response.status == 302 and response['location']:
            return response['location']

        raise CodeUploadError(response.status, content)
