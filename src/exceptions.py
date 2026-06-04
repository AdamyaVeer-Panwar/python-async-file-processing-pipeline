class UnsupportedExtensionError(Exception):
    """
    Raised when a file extension is not allowed.
    """

    pass


class FileTooLargeError(Exception):
    """
    Raised when a file exceeds the configured size limit.
    """

    pass