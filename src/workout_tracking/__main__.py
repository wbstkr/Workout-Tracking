from argparse import ArgumentParser
from workout_tracking import file_handler


def main():
    """Reads a Markdown note, isolates the gym section, and then parses each line into exercise data."""

    # set up command line argument parsing
    cli_parser = ArgumentParser(
        description="Extract and parse plain text workout data from markdown files."
    )
    cli_parser.add_argument(
        "filepath", help="The absolute or relative path to the markdown file."
    )
    cli_args = cli_parser.parse_args()

    todays_workout = file_handler.parse_file(cli_args.filepath)

    print(todays_workout)


if __name__ == "__main__":
    main()
