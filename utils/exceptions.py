class InvalidExpiryError(Exception):
    def __init__(self, expiry):
        self.expiry = expiry

    def __str__(self):
        return repr('expiry [{}] is not a valid value.'.format(self.expiry))

class LanguageNotFoundError(Exception):
    def __init__(self, language):
        self.language = language

    def __str__(self):
        return repr('provided language [{}] is not supported.'.format(self.language))

class NoCodeError(Exception):
    def __init__(self):
        self.message = 'no code has been provided.'

    def __str__(self):
        return repr(self.message)

class CodeUploadError(Exception):
    def __init__(self, status, content):
        self.status = status
        self.content = content

    def __str__(self):
        return repr('code upload failed with status: {}'.format(self.status))
