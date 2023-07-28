"""
Montagem de Layouts para calculadora de e-commerce:

Criado por Victor G. Hermogenes.
"""
# Importações
import PySimpleGUI as Sg
from currency_exchange import currecy_exchange


def mkup_layout():
    # Escolher o tema
    Sg.theme('DarkBlack')

    # Layout
    layout_mkup = [
        [Sg.Text('This app serves to help you \ndiscovering for how much you want to sell')],
        [Sg.Button('Currency Analysis')],
        [Sg.Text('Insert your numbers:')],
        [Sg.Text('Cost:', size=(16, 1)), Sg.Input('0', key='custo', size=(8, 1))],
        [Sg.Text('Mark Up:', size=(16, 1)), Sg.Input('0', key='mkup', size=(8, 1))],
        [Sg.Text('Freight:', size=(16, 1)), Sg.Input('0', key='frete', size=(8, 1))],
        [Sg.Text('Ignore if you not paying freights.')],
        [Sg.Text('Equations:')],
        [Sg.Output(key='calculo', size=(40, 4))],
        [Sg.Button('Run'), Sg.CloseButton('Back', button_color=('black', 'lightgray'))],
        [Sg.Text('Created by Victor G. Hermogenes.')]
    ]

    # Window
    window_mkup = Sg.Window('Choose a MarkUp', layout_mkup, location=(350, 0))

    # Events
    while True:
        # Ler eventos
        event_mkup, values_mkup = window_mkup.read()

        # Fechar janela caso necessário
        if event_mkup == 'Back' or event_mkup == Sg.WIN_CLOSED:
            break

        # Análise de Câmbio
        elif event_mkup == 'Currency Analysis':
            currecy_exchange()

        # Seguir com os cálculos
        elif event_mkup == 'Run':
            try:
                # Situação sem frete
                if values_mkup['frete'] == '':
                    custo = round(float(values_mkup['custo'].replace(',', '.')), 2)
                    mkup = round(float(values_mkup['mkup'].replace(',', '.').replace('%', ''))/100, 2)
                    frete_z = 0
                    calculo_sf = f"""step1 = {custo}+({custo}*{mkup})+{frete_z}
step2 = {custo}+{custo * mkup}+{frete_z}
step3 = {custo + (custo * mkup)}+{frete_z}
result = R$ {custo + (custo * mkup) + frete_z}""".replace('.', ',')
                    window_mkup['calculo'].update(calculo_sf)

                # Situação com frete
                else:
                    custo = round(float(values_mkup['custo'].replace(',', '.')), 2)
                    mkup = round(float(values_mkup['mkup'].replace(',', '.').replace('%', ''))/100, 2)
                    frete = round(float(values_mkup['frete'].replace(',', '.')), 2)
                    calculo = f"""step1 = {custo}+({custo}*{mkup})+{frete}
step2 = {custo}+{custo*mkup}+{frete}
step3 = {custo+(custo*mkup)}+{frete}
result = R$ {custo+(custo*mkup)+frete}""".replace('.', ',')
                    window_mkup['calculo'].update(calculo)

            except ValueError:
                Sg.Popup('Impossible to calculate without charge or Mark Up, try again', location=(350, 0))

    window_mkup.close()


def checar_lqd():
    # Escolher o tema
    Sg.theme('DarkBlack')

    # Layout
    layout_lqd = [
        [Sg.Text('This calculator will help you figure out how much is \nleft over from your sale')],
        [Sg.Text('Fill in the details below')],
        [Sg.Text('Gross sale price:', size=(20, 1)), Sg.Input('0', key='bruto', size=(8, 1))],
        [Sg.Text('Commission percentage:', size=(20, 1)), Sg.Input('0', key='comissao', size=(8, 1))],
        [Sg.Text('Product cost:', size=(20, 1)), Sg.Input('0', key='custo', size=(8, 11))],
        [Sg.Text('Taxes', size=(20, 1)), Sg.Input('0', key='txfixa', size=(8, 11))],
        [Sg.Text('Shipping paid by customer:', size=(20, 1)), Sg.Input('0', key='frtcliente', size=(8, 11))],
        [Sg.Text('Shipping paid by you:', size=(20, 1)), Sg.Input('0', key='frtvc', size=(8, 11))],
        [Sg.Text('NOTE: IF THERE IS NO FEE OR SHIPPING, IGNORE')],
        [Sg.Text('Calculation steps:')],
        [Sg.Output(key='calculo', size=(45, 6))],
        [Sg.Button('Run'), Sg.CloseButton('Back', button_color=('black', 'lightgray'))],
        [Sg.Text('Created by Victor G. Hermogenes.')]
    ]

    # Window
    window_lqd = Sg.Window('Check Profit', layout_lqd, location=(350, 0))

    # Events
    while True:
        # ler eventos
        event_lqd, values_lqd = window_lqd.read()

        # Fechar janela caso necessário
        if event_lqd == 'Back' or event_lqd == Sg.WIN_CLOSED:
            break

        # Seguir com os cálculos:
        elif event_lqd == 'Run':
            try:
                bruto = round(float(values_lqd['bruto'].replace(',', '.')), 2)
                comissao = round(float(values_lqd['comissao'].replace(',', '.').replace('%', '')), 2) / 100
                txfixa = round(float(values_lqd['txfixa'].replace(',', '.')), 2)
                frtcliente = round(float(values_lqd['frtcliente'].replace(',', '.')), 2)
                frtvc = round(float(values_lqd['frtvc'].replace(',', '.')), 2)
                custo = round(float(values_lqd['custo'].replace(',', '.')), 2)
                calculo = f"""step1 = {bruto}-({bruto}*{comissao})-{txfixa}+({frtcliente}-{frtvc})-{custo}
step2 = {bruto}-{round(bruto*comissao, 2)}-{txfixa}+{round(frtcliente-frtvc, 2)}-{custo}
step3 = {round(bruto-(bruto*comissao), 2)}-{round(txfixa+(frtcliente-frtvc), 2)}-{custo}
step4 = {round(bruto-(bruto*comissao)-(txfixa+frtcliente-frtvc), 2)}-{custo}
result = R$ {round(bruto-(bruto*comissao)-txfixa+(frtcliente-frtvc)-custo, 2)}
percentage = {round(((bruto-(bruto*comissao)-txfixa+(frtcliente-frtvc))/custo-1)*100, 2)}%""".replace('.', ',')
                window_lqd['calculo'].update(calculo)

            except ValueError:
                Sg.Popup('Impossible to calculate, one of the fields is empty! Try again', location=(350, 0))
                break

    window_lqd.close()


def descobrir_promocao():
    # Escolher tema
    Sg.theme('DarkBlack')
    # Layout
    layout_pmc = [
        [Sg.Text("""This calculator is for figuring out how much of your price you need to increase to
                    offer the promotion you want.""")],
        [Sg.Text('Regular price:', size=(20, 1)), Sg.Input('0', key='normal', size=(8, 1))],
        [Sg.Text('Promotion Margin:', size=(20, 1)), Sg.Input('0', key='margem', size=(8, 1))],
        [Sg.Text('Freight:', size=(20, 1)), Sg.Input('0', key='frete', size=(8, 1))],
        [Sg.Text('NOTE: IF THERE IS NO SHIPPING, IGNORE')],
        [Sg.Text('Calculation steps:')],
        [Sg.Output(key='calculo', size=(45, 5))],
        [Sg.Button('Run'), Sg.Button('Back', button_color=('black', 'lightgray'))],
        [Sg.Text('Created by Victor G. Hermogenes.')]
    ]

    # Window
    window_pmc = Sg.Window('Descobrir preço de promoção', layout_pmc, location=(350, 0))

    # Ler eventos
    while True:
        event_pmc, values_pmc = window_pmc.read()

        # Fechar caso necessário
        if event_pmc == 'Back' or event_pmc == Sg.WIN_CLOSED:
            break

        # Seguir com os cálculos
        elif event_pmc == 'Run':
            try:
                normal = round(float(values_pmc['normal'].replace(',', '.')), 2)
                margem = round(float(values_pmc['margem'].replace(',', '.').replace('%', '')), 2)
                frete = round(float(values_pmc['frete'].replace(',', '.')), 2)
                calculo = f"""step1 = ({normal}+{frete})/(1-({margem}/100))
step2 = {round(normal+frete, 2)}/(1-{round(margem/100, 2)})
step3 = {round(normal+frete, 2)}/{round(1-(margem/100), 2)}
result = R$ {round((normal+frete)/(1-(margem/100)), 2)}""".replace('.', ',')
                window_pmc['calculo'].update(calculo)
            except ValueError:
                Sg.Popup('Impossible to calculate, one of the fields is empty! Try again', location=(350, 0))
                break

    window_pmc.close()


def decobrir_bruto():
    # Escolher tema
    Sg.theme('DarkBlack')

    # Layout
    layout_bt = [
        [Sg.Text('This calculator serves to take the promotion margin out of your price.')],
        [Sg.Text('Current price:', size=(20, 1)), Sg.Input('0', key='preco', size=(8, 1))],
        [Sg.Text('Promotion percentage:', size=(20, 1)), Sg.Input('0', key='promocao', size=(8, 1))],
        [Sg.Text('Calculation steps:')],
        [Sg.Output(key='calculo', size=(45, 4))],
        [Sg.Button('Run'), Sg.Button('Back', button_color=('black', 'lightgrey'))],
        [Sg.Text('Created by Victor G. Hermogenes.')]
    ]

    # Window
    window_bt = Sg.Window('Discover gross price (no promotion)', layout_bt, location=(350, 1))

    # Ler eventos
    while True:
        event_bt, values_bt = window_bt.read()

        # Fechar caso necessário
        if event_bt == 'Back' or event_bt == Sg.WIN_CLOSED:
            break

        # Seguir com os cálculos
        elif event_bt == 'Run':
            try:
                preco = round(float(values_bt['preco'].replace(',', '.')), 2)
                promocao = round(float(values_bt['promocao'].replace(',', '.').replace('%', '')), 2)/100
                calculo = f"""step1 = {preco}-({preco}*{promocao})
step2 = {preco}-{round(preco*promocao, 2)}
result = R$ {round(preco-(preco*promocao), 2)}""".replace('.', ',')
                window_bt['calculo'].update(calculo)
            except ValueError:
                Sg.Popup('Impossible to calculate, one of the fields is empty! Try again', location=(350, 0))
                break

    window_bt.close()


def diferenca_de_preco():
    # Escolher o tema
    Sg.theme('DarkBlack')

    # Layout
    layout_dif = [
        [Sg.Text('This calculator is for you to discover the gross difference\n and in percentage of your competitor')],
        [Sg.Text('Lower value:', size=(15, 1)), Sg.Input('0', key='menor', size=(8, 1))],
        [Sg.Text('Highest value:', size=(15, 1)), Sg.Input('0', key='maior', size=(8, 1))],
        [Sg.Text('Calculation steps:')],
        [Sg.Output(key='calculo', size=(45, 3))],
        [Sg.Button('Run'), Sg.Button('Back', button_color=('black', 'lightgrey'))],
        [Sg.Text('Created by Victor G. Hermogenes.')]
    ]

    # Window
    window_dif = Sg.Window('Difference in values (between you and the competitor)', layout_dif, location=(350, 0))

    # Ler eventos
    while True:
        event_dif, values_dif = window_dif.read()

        # Fechar caso necessário
        if event_dif == 'Back' or event_dif == Sg.WIN_CLOSED:
            break
        elif event_dif == 'Run':
            try:
                menor = round(float(values_dif['menor'].replace(',', '.')), 2)
                maior = round(float(values_dif['maior'].replace(',', '.')), 2)
                calculo = f"""step1 = {maior}-{menor} | ({menor}/{maior}-1)*-1
result = R$ {round(maior-menor, 2)} | {round(((menor/maior-1)*-1)*100,2)}%""".replace('.', ',')
                window_dif['calculo'].update(calculo)
            except ValueError:
                Sg.Popup('Impossible to calculate, one of the fields is empty! Try again', location=(350, 0))
                break

    window_dif.close()
