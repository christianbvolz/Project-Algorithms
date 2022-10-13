def study_schedule(permanence_period, target_time):
    try:
        students = 0
        for (entrance, exit) in permanence_period:
            if entrance <= target_time <= exit:
                students += 1
    except TypeError or ValueError:
        return None
    else:
        return students
