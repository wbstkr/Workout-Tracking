"""Command-line interface and main orchestration module for the workout tracking ETL
pipeline."""

from argparse import ArgumentParser
import json
from pathlib import Path
from workout_tracking import batch_handler, file_handler


def main():
    """Reads a Markdown note, isolates the gym section, and then parses each line into
    exercise data."""

    # set up command line argument parsing
    cli_parser = ArgumentParser(
        description="Extract and parse plain text workout data from Markdown files."
    )
    cli_parser.add_argument(
        "paths", nargs="+", help="Files and/or directories to parse."
    )
    cli_parser.add_argument(
        "-f",
        "--filter",
        default="*",
        help="Filename pattern to match when scanning directories (default: *).",
    )
    cli_parser.add_argument(
        "-H",
        "--heading",
        default="Workout",
        help="The Markdown heading to search for (default: Workout).",
    )
    cli_parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="Recursively scan any provided directories.",
    )
    cli_args = cli_parser.parse_args()

    unique_file_paths = batch_handler.compile_paths(
        cli_args.paths, cli_args.filter, cli_args.recursive
    )

    cwd = Path.cwd()

    workouts = {
        str(unique_file_path.relative_to(cwd, walk_up=True)): file_handler.parse_file(
            unique_file_path, cli_args.heading
        )
        for unique_file_path in unique_file_paths
    }

    print(json.dumps(workouts, indent=2))


if __name__ == "__main__":
    main()
