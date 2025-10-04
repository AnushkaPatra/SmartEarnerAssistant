import PySimpleGUI as sg
from weather import read_weather_scores, predict_weather_for_city_model

# --- PySimpleGUI layout ---
layout = [
    [sg.Text("Weather CSV File:"), sg.InputText(key="-FILE-"), sg.FileBrowse(file_types=(("CSV Files", "*.csv"),))],
    [sg.Button("Show Weather Scores"), sg.Button("Train Model")],
    [sg.Text("Output:"), sg.Multiline(size=(60, 20), key="-OUTPUT-")],
]

window = sg.Window("Weather Predictor", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "Show Weather Scores":
        try:
            df = read_weather_scores(values["-FILE-"])
            window["-OUTPUT-"].update(df[["date", "city_id", "weather", "weather_idx"]].to_string(index=False))
        except Exception as e:
            sg.popup_error(f"Error: {e}")
    elif event == "Train Model":
        try:
            acc, preds = predict_weather_for_city_model(values["-FILE-"])
            window["-OUTPUT-"].update(f"Model Accuracy: {acc:.2f}\nSample Predictions: {preds}")
        except Exception as e:
            sg.popup_error(f"Error: {e}")

window.close()
