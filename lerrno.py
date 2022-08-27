import sys


def raise_err(err):
    err._err()


def at_format(atline, file: str, codeline: str):
    return f"{atline}::{file} -> {codeline}"


class Error:
    def __init__(self, error: str, at: str):
        self.error = error
        self.at = at

    def _err(self):
        sys.stderr.write(f"FrostPL Exception: {self.error} at {self.at} \n")
        sys.stderr.flush()
