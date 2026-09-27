def parse_exercise_line(line):
    split_exercise = line.split()

    exercise_name = ""
    exercise_type = ""
    exercise_reps = []

    current_weight = 0
    current_unit = ""

    for word in split_exercise:
        if word.isalpha() and word != "bw":
            exercise_name += " " + word
        elif word == "bw":
            exercise_type = "body weight"
        elif word.endswith(("lbs", "kgs")):
            exercise_type = "isotonic"
            current_weight = int("".join([char for char in word if char.isdigit()]))
            current_unit = "".join([char for char in word if char.isalpha()])
        elif word.endswith("s"):
            exercise_type = "isometric"
            rep = int(word[:-1])
            exercise_reps.append({"unit": "seconds", "rep": rep})
        else:
            rep = int(word)
            if exercise_type == "isotonic":
                exercise_reps.append(
                    {"unit": current_unit, "weight": current_weight, "rep": rep}
                )
            elif exercise_type == "body weight":
                exercise_reps.append({"rep": rep})

    exercise_name = exercise_name[1:]

    return {"name": exercise_name, "type": exercise_type, "reps": exercise_reps}
