import PySimpleGUI as sg

feet_label = sg.Text("Enter Feet:")
feet_input = sg.Input(key="feet")

inches_label = sg.Text('Enter Inches:')
inches_input = sg.Input(key="inches")

convert_button = sg.Button("Convert")
output_label = sg.Text(key="output")

window = sg.Window("Convertor", layout=[
                                    [feet_label, feet_input],
                                    [inches_label, inches_input],
                                    [convert_button, output_label]])
while True:
    event, values = window.read()
    match event:
        case 'Convert':
            feet = float(values["feet"])
            inches = float(values['inches'])
            meters = feet * 0.3048 + inches * 0.0254
            window["output"].update(meters)
        case sg.WINDOW_CLOSED:
            break

window.close()