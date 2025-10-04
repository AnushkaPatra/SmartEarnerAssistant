import main

def calculate_weather_score():
    weather = data['weather']
    
    if weather == "clear":
        weather_idx = 0
    elif weather == "rain":
        weather_idx = 1
    else:
        weather_idx = 2 

    return