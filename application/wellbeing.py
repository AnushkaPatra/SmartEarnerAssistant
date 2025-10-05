def ride_score(duration):
    """
    Returns a score from 1 to 5 based on ride duration thresholds:
    Thresholds:
    1: 0-21
    2: 22-43
    3: 44-65
    4: 66-87
    5: 88-110

    """
    try:
        duration = float(duration) 
    except ValueError:
        return "Invalid input"
    
    if 0 <= duration <= 21:
        return 1
    elif 22 <= duration <= 43:
        return 2
    elif 44 <= duration <= 65:
        return 3
    elif 66 <= duration <= 87:
        return 4
    else:
        return 5

