class HttpException(Exception):
    def __init__(self, message: str, name: str, status_code: int) -> None:
        super().__init__(message)
        self.message = message
        self.name = name
        self.status_code = status_code
