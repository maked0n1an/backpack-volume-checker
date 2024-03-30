import os
from typing import List


def format_output(message: str):
    print(f"{message:^80}")


def join_path(path: str | tuple | list) -> str:
    if isinstance(path, str):
        return path
    return str(os.path.join(*path))


def read_txt(path: str | tuple | list) -> List[str]:
    path = join_path(path)
    with open(path, 'r') as file:
        return [row.strip() for row in file]
