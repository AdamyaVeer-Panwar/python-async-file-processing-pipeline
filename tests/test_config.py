from pathlib import Path
import sys
from pathlib import Path as _Path

import pytest
from pydantic import ValidationError  # type: ignore[import]

# Ensure local project directory is on sys.path so `config` can be imported
sys.path.insert(0, str(_Path(__file__).resolve().parent))

from src.config import FileConfig


def test_valid_config():
    config = FileConfig(
        input_dir=Path("data"),
        allowed_extensions=[".csv", ".txt"],
        max_size=1000,
    )

    assert config.input_dir == Path("data")
    assert config.allowed_extensions == [
        ".csv",
        ".txt",
    ]
    assert config.max_size == 1000


def test_negative_max_size():
    with pytest.raises(ValidationError):
        FileConfig(
            input_dir=Path("data"),
            allowed_extensions=[".csv"],
            max_size=-100,
        )


def test_zero_max_size():
    with pytest.raises(ValidationError):
        FileConfig(
            input_dir=Path("data"),
            allowed_extensions=[".csv"],
            max_size=0,
        )


def test_invalid_max_size_type():
    with pytest.raises(ValidationError):
        FileConfig(
            input_dir=Path("data"),
            allowed_extensions=[".csv"],
            max_size="invalid",
        )