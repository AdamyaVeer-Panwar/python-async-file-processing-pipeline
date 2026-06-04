from pathlib import Path

from pydantic import BaseModel, Field


class FileConfig(BaseModel):
    """
    Application configuration.
    """

    input_dir: Path

    allowed_extensions: list[str]

    max_size: int = Field(
        gt=0,
        description="Maximum allowed file size in bytes.",
    )