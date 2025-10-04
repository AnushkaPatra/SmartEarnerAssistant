import PySimpleGUI as sg

layout = [[sg.Text("Hello! This is a blank window.")]]
window = sg.Window("Blank Window", layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break

window.close()
