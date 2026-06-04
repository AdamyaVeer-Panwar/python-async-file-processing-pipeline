from pathlib import Path

import aiofiles  # type: ignore

from src.models import FileMetadata


def get_metadata(path: Path) -> FileMetadata:
    """
    Extract metadata from a file.
    """

    return FileMetadata(
        filename=path.name,
        extension=path.suffix,
        size=path.stat().st_size,
        path=path,
    )


async def read_file(path: Path) -> str:
    """
    Read file contents asynchronously.
    """

    async with aiofiles.open(
        path,
        mode="r",
        encoding="utf-8",
    ) as file:
        return await file.read()