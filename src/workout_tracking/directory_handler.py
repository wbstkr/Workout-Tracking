from pathlib import Path
from workout_tracking import file_handler


def parse_directory(dirpath, file_pattern="*", recursive=False):
    """Compiles a list of workouts in a specified directory, given a filter, and checked recursively as specified.

    Args:
        dirpath (str): The path to the directory being checked.
        file_pattern (str, optional): An optional filename string pattern. Defaults to "*".
        recursive (bool, optional): An optional boolean indicating whether to check the directory recursively. Defaults to False.

    Returns:
        dict: A dictionary mapping each filename to its compiled workout data.
    """

    target_dir = Path(dirpath)

    # compile files in target directory filtered with filter and based on recursive
    target_files = (
        target_dir.rglob(f"{file_pattern}.md")
        if recursive
        else target_dir.glob(f"{file_pattern}.md")
    )

    # parse each file
    workouts = {
        target_file.stem: file_handler.parse_file(target_file)
        for target_file in target_files
    }

    return workouts
