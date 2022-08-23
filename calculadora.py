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
    [Sg.Text('Escolha uma das opções abaixo:')],
    [Sg.Button('Escolher um MarkUp', button_color=('black', 'lightgrey'))],
    [Sg.Button('Checar liquidez', button_color=('black', 'lightgrey'))],
    [Sg.Button('Descobrir preço de promoção', button_color=('black', 'lightgrey'))],
    [Sg.Button('Descobrir preço bruto (sem promoção)', button_color=('black', 'lightgrey'))],
    [Sg.Button('Diferença de valores (entre você e o concorrente)', button_color=('black', 'lightgrey'))],
    [Sg.Button('Sair', button_color=('white', 'darkred'))]
]

# Window
window = Sg.Window('Calculadoras', layout, location=(0, 0))

# Events
while True:
    event, values = window.read()
    if event == 'Sair' or event == Sg.WIN_CLOSED:
        break
    elif event == 'Escolher um MarkUp':
        lt.mkup_layout()
    elif event == 'Checar liquidez':
        lt.checar_lqd()
    elif event == 'Descobrir preço de promoção':
        lt.descobrir_promocao()
    elif event == 'Descobrir preço bruto (sem promoção)':
        lt.decobrir_bruto()
    elif event == 'Diferença de valores (entre você e o concorrente)':
        lt.diferenca_de_preco()

window.close()
