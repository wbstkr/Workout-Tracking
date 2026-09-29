import parser


def parse_file(filepath):
    """Reads a markdown note, isolates the gym section, and then parses each line into exercise data.

    Args:
        filepath (str): The path to the markdown file.

    Returns:
        list: A list containing parsed workout data.
    """

    # load note and strip whitespace
    with open(filepath, "r") as file:
        lines = file.readlines()
    stripped_lines = [line.strip() for line in lines]

    # initialize helper variables
    parsed_workout = []

    # isolate gym section
    gym_section = extract_section(stripped_lines, "Gym")

    # convert the raw exercise strings in the gym section into parsed exercise data
    for raw_exercise_string in gym_section:
        parsed_exercise = parser.parse_raw_exercise_string(raw_exercise_string)
        parsed_workout.append(parsed_exercise)

    return parsed_workout


def extract_section(str_list, heading_string):
    """Extracts all strings in a list that belong to a specific heading.

    Args:
        str_list (list): A list of strings, usually read from a markdown file, that is to be extracted.
        heading_string (str): The name of the heading.

    Returns:
        list: A list containing all strings that belong to the requested heading.
    """

    # initialize helper variables
    is_target_section = False
    extracted_section = []

    for line in str_list:
        # indicate that gym section has been reached
        if line == f"# {heading_string}":
            is_target_section = True
            continue

            # indicate that gym section has been exhausted
        if line.startswith("#") and line != f"# {heading_string}":
            is_target_section = False

            # store exercise into gym_section when in gym section
        if is_target_section and line != "":
            extracted_section.append(line)

    return extracted_section
