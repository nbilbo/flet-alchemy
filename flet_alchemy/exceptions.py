class FieldException(Exception):
    def __init__(self, message: str, field: str) -> None:
        super().__init__(message)
        self.field = field
