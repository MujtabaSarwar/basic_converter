# Convert one unit to another---coded by Mujtaba Sarwar Sina---
# This program is the updated version of basic_converter..

'''UPDATE- previous program of basic_converter couldn't take any floating point input.
it could only return converted result if given integer numbers. otherwise it tells to enter a numeric values. But this udated version of program can convert the floating point number besides integers.It only ask for numeric value if you enter string.

-----pardon my english grammatical mistake..English is not my native language----
'''


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
        try:
            if float(input_value):
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
        except:
            my_window['-OUTPUT-'].update('Please, enter a numeric value')

my_window.close()
