def calculate_fine(extra_days):
    fine = 0    
    week = 1

    while extra_days > 0:
        days_in_week = min(7, extra_days)
        fine += days_in_week * (10 * week)
        extra_days -= days_in_week
        week += 1

    return fine