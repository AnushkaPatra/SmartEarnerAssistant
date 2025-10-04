def weekly_bonus(current_progress, goal):
    difference = current_progress - goal
    
    status = -1

    if (difference < 0):
        status = 1
        print("You have not reached your weekly bonus")
        print("Job left: ", difference * -1)
    else:
        status = 0
        print("Your have reached your weekly bonus")
    
    return status