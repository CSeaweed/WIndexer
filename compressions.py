import zlib


def compress(string: str) -> bytes:
    result: bytes = zlib.compress(string.encode())
    return result

def decompress(string: str) -> str:
    result: str = zlib.decompress(string).decode()
    return result