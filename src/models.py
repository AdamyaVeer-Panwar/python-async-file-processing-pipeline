from dataclasses import dataclass
from enum import Enum
from pathlib import Path


class ProcessingStatus(Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    SKIPPED = "SKIPPED"


@dataclass(slots=True)
class FileMetadata:
    """
    Metadata extracted from a file.
    """

    filename: str
    extension: str
    size: int
    path: Path


@dataclass(slots=True)
class ProcessingResult:
    """
    Result of processing a file.
    """

    metadata: FileMetadata | None
    status: ProcessingStatus
    duration_ms: float
    error_message: str | None