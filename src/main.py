import asyncio
from pathlib import Path

from src.config import FileConfig
from src.processor import process_file


async def main() -> None:
    config = FileConfig(
        input_dir=Path("data"),
        allowed_extensions=[
            ".csv",
            ".txt",
        ],
        max_size=1_000_000,
    )

    files = [
        path
        for path in config.input_dir.iterdir()
        if path.is_file()
    ]

    for path in files:
        print(path)

    tasks = [
        process_file(path, config)
        for path in files
    ]

    results = await asyncio.gather(*tasks)

    for result in results:
        print(result)


if __name__ == "__main__":
    asyncio.run(main())