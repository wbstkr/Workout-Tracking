def parse_raw_exercise_string(raw_exercise_string):
    """Converts a raw exercise string into a parsed exercise dictionary containing an exercise name, an exercise type, and list of sets.

    Args:
        raw_exercise_string (str): A string containing raw exercise data.

    Returns:
        dict: A dictionary containing:
            - 'name' (str): The exercise name.
            - 'type' (str): The classification ('isotonic', 'body weight', or 'isometric').
            - 'sets' (list): A list of dictionaries representing individual sets.
    """

    # split raw string into words
    words = raw_exercise_string.split()

    # initialize variables
    exercise_name_parts = []
    exercise_type = ""
    exercise_sets = []

    # initialize helper variables
    current_weight = 0
    current_unit = ""

    # parse through words to populate dictionary members
    for word in words:
        # indicate that exercise is rep based if weight is indicated as body weight
        if word == "bw":
            exercise_type = "body weight"

        # indicate that exercise is weight based and therefore isotonic if weight is indicated with units
        elif word.endswith(("lbs", "kgs")) and word[:-3].isdigit():
            exercise_type = "isotonic"
            current_unit = word[-3:]
            current_weight = int(word[:-3])

        # indicate that exercise is time based and therefore isometric if set is indicated in terms of seconds
        elif word.endswith("s") and word[:-1].isdigit():
            exercise_type = "isometric"
            duration = int(word[:-1])

            # record isometric set
            exercise_sets.append({"unit": "seconds", "duration": duration})

        # record body weight and isotonic set
        elif word.isdigit():
            rep = int(word)
            if exercise_type == "isotonic":
                exercise_sets.append(
                    {"unit": current_unit, "weight": current_weight, "rep": rep}
                )
            elif exercise_type == "body weight":
                exercise_sets.append({"rep": rep})

        # add to exercise name builder
        else:
            exercise_name_parts.append(word)

    # construct exercise name by joining parts
    exercise_name = " ".join(exercise_name_parts)

    # return structured data
    return {"name": exercise_name, "type": exercise_type, "sets": exercise_sets}
