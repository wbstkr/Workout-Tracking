from parser import parse_raw_exercise_string


def main():
    """Reads a markdown note, isolates the gym section, and then parses each line into exercise data."""

    # load note and strip whitespace
    with open("data/test_note.md", "r") as file:
        lines = file.readlines()
    stripped_lines = [line.strip() for line in lines]

    # initialize variables
    is_gym_section = False
    gym_section = []
    todays_workout = []

    # isolate gym section
    for line in stripped_lines:
        # indicate that gym section has been reached
        if line == "# Gym":
            is_gym_section = True
            continue
        
        # indicate that gym section has been exhausted
        if line.startswith("#") and line != "# Gym":
            is_gym_section = False
        
        # store exercise into gym_section when in gym section
        if is_gym_section and line != "":
            gym_section.append(line)

    # convert the raw exercise strings in the gym section into parsed exercise data
    for raw_exercise_string in gym_section:
        parsed_exercise = parse_raw_exercise_string(raw_exercise_string)
        todays_workout.append(parsed_exercise)

    print(todays_workout)


if __name__ == "__main__":
    main()
