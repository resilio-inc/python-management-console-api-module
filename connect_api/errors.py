
class ApiError(Exception):
    def __init__(self, message, cause=None):
        super(ApiError, self).__init__(message)
        self.cause = cause
        self.message = message

    def error_name(self):
        return 'Api error'

    def __str__(self):
        return '{}: {}'.format(self.error_name(), self.message)


class ApiConnectionError(ApiError):
    def error_name(self):
        return 'Connection error'


class ApiUnauthorizedError(ApiError):
    def error_name(self):
        return 'Unauthorized error'