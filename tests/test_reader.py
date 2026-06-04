from pathlib import Path

import pytest

from src.reader import (
    get_metadata,
    read_file,
)


def test_get_metadata():
    path = Path(__file__)

    metadata = get_metadata(path)

    assert metadata.filename == path.name
    assert metadata.extension == path.suffix
    assert metadata.size > 0
    assert metadata.path == path


@pytest.mark.asyncio
async def test_read_file():
    path = Path(__file__)

    content = await read_file(path)

    assert isinstance(content, str)
    assert len(content) > 0