from pathlib import Path

import pytest

from config import FileConfig
from models import ProcessingStatus
from processor import process_file


@pytest.mark.asyncio
async def test_process_file_success():
    config = FileConfig(
        input_dir=Path("."),
        allowed_extensions=[".py"],
        max_size=1_000_000,
    )

    result = await process_file(
        Path(__file__),
        config,
    )

    assert result.status == ProcessingStatus.SUCCESS

    assert result.metadata is not None

    assert result.error_message is None


@pytest.mark.asyncio
async def test_unsupported_extension():
    config = FileConfig(
        input_dir=Path("."),
        allowed_extensions=[".csv"],
        max_size=1_000_000,
    )

    result = await process_file(
        Path(__file__),
        config,
    )

    assert result.status == ProcessingStatus.FAILED

    assert result.metadata is None

    assert result.error_message is not None

    assert "not allowed" in result.error_message


@pytest.mark.asyncio
async def test_missing_file():
    config = FileConfig(
        input_dir=Path("."),
        allowed_extensions=[".csv"],
        max_size=1_000_000,
    )

    result = await process_file(
        Path(
            "this_file_should_not_exist.csv"
        ),
        config,
    )

    assert result.status == ProcessingStatus.FAILED

    assert result.metadata is None

    assert result.error_message is not None


@pytest.mark.asyncio
async def test_file_too_large():
    config = FileConfig(
        input_dir=Path("."),
        allowed_extensions=[".py"],
        max_size=1,
    )

    result = await process_file(
        Path(__file__),
        config,
    )

    assert result.status == ProcessingStatus.FAILED

    assert result.metadata is None

    assert result.error_message is not None

    assert "size limit" in result.error_message