# Convert one unit to another---coded by Mujtaba Sarwar Sina---
import PySimpleGUI as sg

layout = [[sg.Text('Enter your input to convert', text_color='indigo', background_color='sky blue')],

          [sg.Input(key='-INPUT-'),
           sg.Spin(['Km-Mile', 'Kg-Pound', 'Second-Minuite'], key='-MENU-'),
           sg.Button('Convert', key='-BUTTON-')
           ],

          [sg.Text('Output', background_color='skyblue', text_color='indigo',
                   enable_events=True, key='-OUTPUT-')]
          ]

my_window = sg.Window('Digital Converter', layout, background_color='black')

while True:
    event, values = my_window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == '-BUTTON-':
        input_value = values['-INPUT-']
        if input_value.isnumeric(): #does not support floating input
            match values['-MENU-']:
                case 'Km-Mile':
                    x = float(input_value)*0.621371
                    out_msg = f"{input_value} Km are {round(x, 2)} Miles"
                case'Kg-Pound':
                    x = float(input_value)*2.20462
                    out_msg = f"{input_value} Kg are {round(x, 2)} Pounds"

                case 'Second-Minuite':
                    x = float(input_value)/60
                    out_msg = f"{input_value} Seconds are {round(x, 2)} Minuits"
            my_window['-OUTPUT-'].update(out_msg)
        else:
            my_window['-OUTPUT-'].update('Please, enter a numeric value')

my_window.close()
