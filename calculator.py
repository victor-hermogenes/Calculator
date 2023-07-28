import PySimpleGUI as Sg
import layouts as lt

"""
Interface principal da Calculadora
"""

"""Montagem do Main Layout"""
# Escolher o tema
Sg.theme('DarkBlack')

# Layout
layout = [
    [Sg.Text('Choose one of the options below:')],
    [Sg.Button('Choose a MarkUp', button_color=('black', 'lightgrey'))],
    [Sg.Button('Check Profit', button_color=('black', 'lightgrey'))],
    [Sg.Button('Choose Sale Promotion Price', button_color=('black', 'lightgrey'))],
    [Sg.Button('Discover Sale Promotion Gross Price', button_color=('black', 'lightgrey'))],
    [Sg.Button('Difference in values (between you and the competitor)', button_color=('black', 'lightgrey'))],
    [Sg.Button('Leave', button_color=('white', 'darkred'))],
    [Sg.Text('Created by Victor G. Hermogenes.')]
]

# Icon
icon_path = 'Icon.ico'

# Window
window = Sg.Window('Calculations', layout, location=(0, 0), icon=icon_path)

# Events
while True:
    event, values = window.read()
    if event == 'Leave' or event == Sg.WIN_CLOSED:
        break
    elif event == 'Choose a MarkUp':
        lt.mkup_layout()
    elif event == 'Check Profit':
        lt.checar_lqd()
    elif event == 'Choose Sale Promotion Price':
        lt.descobrir_promocao()
    elif event == 'Discover Sale Promotion Gross Price':
        lt.decobrir_bruto()
    elif event == 'Difference in values (between you and the competitor)':
        lt.diferenca_de_preco()

window.close()
