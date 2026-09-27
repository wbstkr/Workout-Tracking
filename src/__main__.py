from parser import parse_exercise_line


def main():
    with open("data/test_note.md", "r") as file:
        lines = file.readlines()

    is_gym_section = False
    todays_workout = []

    for line in lines:
        clean_line = line.strip()
        if clean_line == "# Gym":
            is_gym_section = True
            continue
        if clean_line.startswith("#") and clean_line != "# Gym":
            is_gym_section = False
        if is_gym_section and clean_line != "":
            parsed_data = parse_exercise_line(clean_line)
            todays_workout.append(parsed_data)

    print(todays_workout)


if __name__ == "__main__":
    main()
