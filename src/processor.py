from pathlib import Path
from time import perf_counter

from src.config import FileConfig
from src.exceptions import (
    FileTooLargeError,
    UnsupportedExtensionError,
)
from src.logger import logger
from src.models import (
    ProcessingResult,
    ProcessingStatus,
)
from src.reader import (
    get_metadata,
    read_file,
)


async def process_file(
    path: Path,
    config: FileConfig,
) -> ProcessingResult:
    """
    Validate and process a file.
    """

    start_time = perf_counter()

    try:
        # Validate extension
        if path.suffix not in config.allowed_extensions:
            raise UnsupportedExtensionError(
                f"Extension '{path.suffix}' is not allowed"
            )

        # Validate size
        if path.stat().st_size > config.max_size:
            raise FileTooLargeError(
                f"File '{path.name}' exceeds size limit"
            )

        metadata = get_metadata(path)

        # Real async I/O
        content = await read_file(path)

        duration_ms = (
            perf_counter() - start_time
        ) * 1000

        logger.info(
            "Successfully processed %s",
            path.name,
        )

        return ProcessingResult(
            metadata=metadata,
            status=ProcessingStatus.SUCCESS,
            duration_ms=duration_ms,
            error_message=None,
        )

    except (
        UnsupportedExtensionError,
        FileTooLargeError,
        FileNotFoundError,
        PermissionError,
        UnicodeDecodeError
    ) as error:

        duration_ms = (
            perf_counter() - start_time
        ) * 1000

        logger.error(
            "Failed to process %s: %s",
            path.name,
            error,
        )

        return ProcessingResult(
            metadata=None,
            status=ProcessingStatus.FAILED,
            duration_ms=duration_ms,
            error_message=str(error),
        )