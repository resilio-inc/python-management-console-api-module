
class ApiError(Exception):
    def __init__(self, *args, **kwargs):
        super(ApiError, self).__init__(*args, **kwargs)
