def parse_raw_exercise_string(raw_exercise_string):
    """Converts a raw exercise string into a parsed exercise dictionary containing an exercise name, an exercise type, and list of sets.

    Args:
        raw_exercise_string (str): string containing raw exercise data

    Returns:
        dict: A dictionary containing:
            - 'name' (str): The exercise name.
            - 'type' (str): The classification ('isotonic', 'body weight', or 'isometric').
            - 'sets' (list): A list of dictionaries representing individual sets.
    """

    # split raw string into words
    words = raw_exercise_string.split()

    # initialize variables
    exercise_name = ""
    exercise_type = ""
    exercise_sets = []

    current_weight = 0
    current_unit = ""

    # parse through words to populate dictionary members
    for word in words:
        # construct exercise name with words until first exercise type indicator or set is reached
        if word.isalpha() and word != "bw":
            exercise_name += " " + word

        # indicate that exercise is rep based if weight is indicated as body weight
        elif word == "bw":
            exercise_type = "body weight"

        # indicate that exercise is weight based and therefore isotonic if weight is indicated with units
        elif word.endswith(("lbs", "kgs")):
            exercise_type = "isotonic"
            current_weight = int("".join([char for char in word if char.isdigit()]))
            current_unit = "".join([char for char in word if char.isalpha()])

        # indicate that exercise is time based and therefore isometric if set is indicated in terms of seconds
        elif word.endswith("s"):
            exercise_type = "isometric"
            rep = int(word[:-1])

            # record isometric set
            exercise_sets.append({"unit": "seconds", "rep": rep})

        # record body weight and isotonic set
        else:
            rep = int(word)
            if exercise_type == "isotonic":
                exercise_sets.append(
                    {"unit": current_unit, "weight": current_weight, "rep": rep}
                )
            elif exercise_type == "body weight":
                exercise_sets.append({"rep": rep})

    # remove leading space remaining from exercise name building loop
    exercise_name = exercise_name[1:]

    # return structured data
    return {"name": exercise_name, "type": exercise_type, "sets": exercise_sets}
