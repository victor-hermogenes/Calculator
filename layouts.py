"""
Montagem de Layouts para calculadora de e-commerce:

Criado por Victor G. Hermogenes.
"""
# Importações
import PySimpleGUI as Sg


def mkup_layout():
    # Escolher o tema
    Sg.theme('DarkBlack')

    # Layout
    layout_mkup = [
        [Sg.Text('This app serves to help you \ndiscovering for how much you want to sell')],
        [Sg.Text('Insert your numbers:')],
        [Sg.Text('Cost:', size=(16, 1)), Sg.Input('0', key='custo', size=(8, 1))],
        [Sg.Text('Mark Up:', size=(16, 1)), Sg.Input('0', key='mkup', size=(8, 1))],
        [Sg.Text('Freight:', size=(16, 1)), Sg.Input('0', key='frete', size=(8, 1))],
        [Sg.Text('Ignore if you not paying freights.')],
        [Sg.Text('Equations:')],
        [Sg.Output(key='calculo', size=(40, 4))],
        [Sg.Button('Run'), Sg.CloseButton('Back', button_color=('black', 'lightgray'))],
    ]

    # Window
    window_mkup = Sg.Window('Escolher um MarkUp', layout_mkup, location=(350, 0))

    # Events
    while True:
        # Ler eventos
        event_mkup, values_mkup = window_mkup.read()

        # Fechar janela caso necessário
        if event_mkup == 'Back' or event_mkup == Sg.WIN_CLOSED:
            break

        # Seguir com os cáclulos
        elif event_mkup == 'Run':
            try:
                # Situação sem frete
                if values_mkup['frete'] == '':
                    custo = round(float(values_mkup['custo'].replace(',', '.')), 2)
                    mkup = round(float(values_mkup['mkup'].replace(',', '.').replace('%', ''))/100, 2)
                    frete_z = 0
                    calculo_sf = f"""1 = {custo}+({custo}*{mkup})+{frete_z}
2 = {custo}+{custo * mkup}+{frete_z}
3 = {custo + (custo * mkup)}+{frete_z}
answer = R$ {custo + (custo * mkup) + frete_z}""".replace('.', ',')
                    window_mkup['calculo'].update(calculo_sf)

                # Situação com frete
                else:
                    custo = round(float(values_mkup['custo'].replace(',', '.')), 2)
                    mkup = round(float(values_mkup['mkup'].replace(',', '.').replace('%', ''))/100, 2)
                    frete = round(float(values_mkup['frete'].replace(',', '.')), 2)
                    calculo = f"""1 = {custo}+({custo}*{mkup})+{frete}
2 = {custo}+{custo*mkup}+{frete}
3 = {custo+(custo*mkup)}+{frete}
answer = R$ {custo+(custo*mkup)+frete}""".replace('.', ',')
                    window_mkup['calculo'].update(calculo)

            except ValueError:
                Sg.Popup('Impossível calcular sem custo ou Mark Up, tente novamete', location=(350, 0))
                break

    window_mkup.close()


def checar_lqd():
    # Escolher o tema
    Sg.theme('DarkBlack')

    # Layout
    layout_lqd = [
        [Sg.Text('Essa calculadora vai te ajudar a descobrir o quanto \nsobrou da sua venda')],
        [Sg.Text('Preencha os dados abaixo')],
        [Sg.Text('Preço bruto da venda:', size=(20, 1)), Sg.Input('0', key='bruto', size=(8, 1))],
        [Sg.Text('Percentual de comissão:', size=(20, 1)), Sg.Input('0', key='comissao', size=(8, 1))],
        [Sg.Text('Custo do produto:', size=(20, 1)), Sg.Input('0', key='custo', size=(8, 11))],
        [Sg.Text('Taxa fixa:', size=(20, 1)), Sg.Input('0', key='txfixa', size=(8, 11))],
        [Sg.Text('Frete pago pelo cliente:', size=(20, 1)), Sg.Input('0', key='frtcliente', size=(8, 11))],
        [Sg.Text('Frete pago por você:', size=(20, 1)), Sg.Input('0', key='frtvc', size=(8, 11))],
        [Sg.Text('OBS: CASO NÃO TENHA TAXA OU FRETE, IGNORAR')],
        [Sg.Text('Etapas do cálculo:')],
        [Sg.Output(key='calculo', size=(45, 6))],
        [Sg.Button('Calcular'), Sg.CloseButton('Voltar', button_color=('black', 'lightgray'))]
    ]

    # Window
    window_lqd = Sg.Window('Checar liquidez', layout_lqd, location=(350, 0))

    # Events
    while True:
        # ler eventos
        event_lqd, values_lqd = window_lqd.read()

        # Fechar janela caso necessário
        if event_lqd == 'Voltar' or event_lqd == Sg.WIN_CLOSED:
            break

        # Seguir com os cálculos:
        elif event_lqd == 'Calcular':
            try:
                bruto = round(float(values_lqd['bruto'].replace(',', '.')), 2)
                comissao = round(float(values_lqd['comissao'].replace(',', '.').replace('%', '')), 2) / 100
                txfixa = round(float(values_lqd['txfixa'].replace(',', '.')), 2)
                frtcliente = round(float(values_lqd['frtcliente'].replace(',', '.')), 2)
                frtvc = round(float(values_lqd['frtvc'].replace(',', '.')), 2)
                custo = round(float(values_lqd['custo'].replace(',', '.')), 2)
                calculo = f"""etapa1 = {bruto}-({bruto}*{comissao})-{txfixa}+({frtcliente}-{frtvc})
etapa2 = {bruto}-{round(bruto*comissao, 2)}-{txfixa}+{(frtcliente-frtvc)}
etapa3 = {round(bruto-(bruto*comissao), 2)}-{round(txfixa+(frtcliente-frtvc), 2)}
resultado = R$ {round(bruto-(bruto*comissao)-txfixa+(frtcliente-frtvc), 2)}
percentual = {round(((bruto-(bruto*comissao)-txfixa+(frtcliente-frtvc))/custo-1)*100, 2)}%""".replace('.', ',')
                window_lqd['calculo'].update(calculo)

            except ValueError:
                Sg.Popup('Impossível calcular, algum dos campos está vazio! Tente novamente', location=(350, 0))
                break

    window_lqd.close()


def descobrir_promocao():
    # Escolher tema
    Sg.theme('DarkBlack')
    # Layout
    layout_pmc = [
        [Sg.Text("""Esta calculadora serve para descobrir o quanto do seu preço você precisa aumentar para
ofertar a promoção que você pretende.""")],
        [Sg.Text('Preço normal:', size=(20, 1)), Sg.Input('0', key='normal', size=(8, 1))],
        [Sg.Text('Margem de promoção:', size=(20, 1)), Sg.Input('0', key='margem', size=(8, 1))],
        [Sg.Text('Frete:', size=(20, 1)), Sg.Input('0', key='frete', size=(8, 1))],
        [Sg.Text('OBS: CASO NÃO TENHA FRETE, IGNORAR')],
        [Sg.Text('Etapas do cálculo:')],
        [Sg.Output(key='calculo', size=(45, 5))],
        [Sg.Button('Calcular'), Sg.Button('Voltar', button_color=('black', 'lightgray'))]
    ]

    # Window
    window_pmc = Sg.Window('Descobrir preço de promoção', layout_pmc, location=(350, 0))

    # Ler eventos
    while True:
        event_pmc, values_pmc = window_pmc.read()

        # Fechar caso necessário
        if event_pmc == 'Voltar' or event_pmc == Sg.WIN_CLOSED:
            break

        # Seguir com os cálculos
        elif event_pmc == 'Calcular':
            try:
                normal = round(float(values_pmc['normal'].replace(',', '.')), 2)
                margem = round(float(values_pmc['margem'].replace(',', '.').replace('%', '')), 2)
                frete = round(float(values_pmc['frete'].replace(',', '.')), 2)
                calculo = f"""etapa1 = ({normal}+{frete})/(1-({margem}/100))
etapa2 = {normal+frete}/(1-{margem/100})
etapa3 = {normal+frete}/{(1-(margem/100))}
resultado = R$ {round((normal+frete)/(1-(margem/100)), 2)}""".replace('.', ',')
                window_pmc['calculo'].update(calculo)
            except ValueError:
                Sg.Popup('Impossível calcular, algum dos campos está vazio! Tente novamente', location=(350, 0))
                break

    window_pmc.close()


def decobrir_bruto():
    # Escolher tema
    Sg.theme('DarkBlack')

    # Layout
    layout_bt = [
        [Sg.Text('Esta calculadora serve para tirar a margem de promoção do seu preço.')],
        [Sg.Text('Preço atual:', size=(20, 1)), Sg.Input('0', key='preco', size=(8, 1))],
        [Sg.Text('Percentual da promoção:', size=(20, 1)), Sg.Input('0', key='promocao', size=(8, 1))],
        [Sg.Text('Etapas do cálculo:')],
        [Sg.Output(key='calculo', size=(45, 4))],
        [Sg.Button('Calcular'), Sg.Button('Voltar', button_color=('black', 'lightgrey'))]
    ]

    # Window
    window_bt = Sg.Window('Descobrir preço bruto (sem promoção)', layout_bt, location=(350, 1))

    # Ler eventos
    while True:
        event_bt, values_bt = window_bt.read()

        # Fechar caso necessário
        if event_bt == 'Voltar' or event_bt == Sg.WIN_CLOSED:
            break

        # Seguir com os cálculos
        elif event_bt == 'Calcular':
            try:
                preco = round(float(values_bt['preco'].replace(',', '.')), 2)
                promocao = round(float(values_bt['promocao'].replace(',', '.').replace('%', '')), 2)/100
                calculo = f"""etapa1 = {preco}-({preco}*{promocao})
etapa2 = {preco}-{round(preco*promocao, 2)}
res = R$ {round(preco-(preco*promocao), 2)}""".replace('.', ',')
                window_bt['calculo'].update(calculo)
            except ValueError:
                Sg.Popup('Impossível calcular, algum dos campos está vazio! Tente novamente', location=(350, 0))
                break

    window_bt.close()


def diferenca_de_preco():
    # Escolher o tema
    Sg.theme('DarkBlack')

    # Layout
    layout_dif = [
        [Sg.Text('Esta calculadora serve para você descobrir a diferença bruta\n e em percentual do seu concorrente')],
        [Sg.Text('Menor valor', size=(15, 1)), Sg.Input('0', key='menor', size=(8, 1))],
        [Sg.Text('Maior valor', size=(15, 1)), Sg.Input('0', key='maior', size=(8, 1))],
        [Sg.Text('Etapas do cálculo')],
        [Sg.Output(key='calculo', size=(45, 3))],
        [Sg.Button('Calcular'), Sg.Button('Voltar', button_color=('black', 'lightgrey'))]
    ]

    # Window
    window_dif = Sg.Window('Diferença de valores (entre você e o concorrente)', layout_dif, location=(350, 0))

    # Ler eventos
    while True:
        event_dif, values_dif = window_dif.read()

        # Fechar caso necessário
        if event_dif == 'Voltar' or event_dif == Sg.WIN_CLOSED:
            break
        elif event_dif == 'Calcular':
            try:
                menor = round(float(values_dif['menor'].replace(',', '.')), 2)
                maior = round(float(values_dif['maior'].replace(',', '.')), 2)
                calculo = f"""etapa1 = {maior}-{menor} | ({menor}/{maior}-1)*-1
resultado = R$ {round(maior-menor, 2)} | {round(((menor/maior-1)*-1)*100,2)}%""".replace('.', ',')
                window_dif['calculo'].update(calculo)
            except ValueError:
                Sg.Popup('Impossível calcular, algum dos campos está vazio! Tente novamente', location=(350, 0))
                break

    window_dif.close()
