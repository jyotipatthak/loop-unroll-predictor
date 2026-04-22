def default_heuristic(row):
    if row['trip_count'] >= 8 and row['body_instr_count'] <= 10:
        return 4
    elif row['trip_count'] >= 4:
        return 2
    return 1