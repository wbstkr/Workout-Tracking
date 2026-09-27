def main():
    test_exercise = "Dumbbell Curls 25lbs 10 5 2 20lbs 9 6 4"
    
    split_exercise = test_exercise.split()
    
    dumbbell_curl = {}
        
    exercise_name = ""
    # isotonic, body weight, isometric
    exercise_type = ""
    exercise_reps = []
    
    current_weight = 0
    current_unit = ""
    
    for word in split_exercise:
        if word.isalpha() and word != "bw":
            exercise_name += ' ' + word
        elif word == "bw":
            exercise_type = "body weight"
        elif word.endswith(("lbs", "kgs")):
            exercise_type = "isotonic"
            current_weight = int("".join([char for char in word if char.isdigit()]))
            current_unit = "".join([char for char in word if char.isalpha()])
        elif word.endswith('s'):
            exercise_type = "isometric"
            rep = int(word[:-1])
            exercise_reps.append({"unit": "seconds", "rep": rep})
        else:
            rep = int(word)
            if exercise_type == "isotonic":
                exercise_reps.append({"unit": current_unit, "weight": current_weight, "rep": rep})
            elif exercise_type == "body weight":
                exercise_reps.append({"rep": rep})
            
    exercise_name = exercise_name[1:]
    
    dumbbell_curl["name"] = exercise_name
    dumbbell_curl["type"] = exercise_type
    dumbbell_curl["reps"] = exercise_reps
    
    print(split_exercise)
    print(exercise_name)
    print(exercise_type)
    print(exercise_reps)
    print(dumbbell_curl)

if __name__ == '__main__':
    main()