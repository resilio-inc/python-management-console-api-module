
class ApiError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ModelException(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)