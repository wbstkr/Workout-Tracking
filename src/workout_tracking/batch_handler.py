"""Compiles mixed input paths into a unique set of Markdown file paths."""

from pathlib import Path


def compile_paths(paths, file_pattern="*", recursive=False):
    """Generates a set of unique file paths to Markdown files by compiling all file
    paths and combing through files in directory paths via provided file pattern,
    recursively as specified.

    Args:
        paths (list): A list of strings representing paths to be compiled.
        file_pattern (str, optional): An optional filename string pattern to filter
            directory paths with. Defaults to "*".
        recursive (bool, optional): An optional boolean indicating whether to check the
            directory recursively. Defaults to False.

    Returns:
        set: A set of unique file paths to Markdown files.
    """

    # initialize output set
    unique_paths = set()

    for path in paths:
        target = Path(path).resolve()

        # check if path exists
        if not target.exists():
            print(f"Skipped: {target} does not exist.")

        # file logic
        elif target.is_file():
            # only accept Markdown files
            if target.suffix == ".md":
                unique_paths.add(target)
            else:
                print(f"Skipped: {target} is not a Markdown file.")

        # dir logic
        elif target.is_dir():
            filtered_paths = set(
                target.rglob(f"{file_pattern}.md")
                if recursive
                else target.glob(f"{file_pattern}.md")
            )

            # throw warning if filtered dir is empty
            if len(filtered_paths) == 0:
                print(
                    f"Skipped: {target} does not contain any files that match {file_pattern}.md."
                )
            else:
                unique_paths.update(filtered_paths)

    return unique_paths
