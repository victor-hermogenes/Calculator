import requests
import PySimpleGUI as sg


def get_exchange_rate(base_currency, target_currency):
    try:
        response = requests.get(f'https://economia.awesomeapi.com.br/last/{base_currency}-{target_currency}')
        data = response.json()
        return data[f'{base_currency}{target_currency}']['bid']

    except ValueError:
        return None


def currecy_exchange():
    sg.theme('DarkBlack')

    layout_currency = [
        [sg.Button('Choose Currency', size=(12, 2)), sg.Input(key='base', size=(12, 1)),
         sg.Input(key='target', size=(12, 1)), sg.Text(key='result', size=(12, 1))],
        [sg.Text('Product price:', size=(12, 1)), sg.Input(0, key='cost', size=(12, 1)),
         sg.Input(key='result_product', size=(12, 1))],
        [sg.Button('Back'), sg.Text(key='warning', size=(50, 1))],
        [sg.Text('Created by Victor G. Hermogenes.')]
    ]

    window = sg.Window('Currency Exchange', layout_currency, location=(680, 0), disable_close=True)

    while True:
        event, values = window.read()

        if event == 'Back' or event == sg.WIN_CLOSED:
            break
        elif event == 'Choose Currency':
            try:
                exchange = float(get_exchange_rate(values['base'], values['target']))
                product_price_value = round(float(values['cost']), 2)
                product_price = round(product_price_value * exchange, 2)
                warning = 'To run "Choose a MarkUp" calculator, please, close this one.'
                window['result'].update(exchange)
                window['result_product'].update(product_price)
                window['warning'].update(warning)
            except Exception as e:
                print("Error occurred:", e)

    window.close()


def get_taxes():
    sg.theme('DarkBlack')

    layout_get_taxes = [
        [sg.Text('Get your raw taxes price in here:')],
        [sg.Text('Sell price:', size=(12, 1)), sg.Input(0, key='rawprice', size=(12, 1)),
         sg.Text('Tax percentage:', size=(12, 1)), sg.Input(0, key='tax%', size=(12, 1)),
         sg.Input(0, key='result', size=(12, 1)), sg.Button('Run')],
        [sg.Button('Back')],
        [sg.Text('Created by Victor G. Hermogenes.')]
    ]

    window_taxes = sg.Window('Get your taxes price:', layout_get_taxes, location=(715, 0), disable_close=True)

    while True:
        event, values = window_taxes.read()

        if event == sg.WIN_CLOSED or event == 'Back':
            break
        if event == 'Run':
            try:
                sell_price = float(values['rawprice'])
                tax = float(values['tax%'].replace('%', '')) / 100
                answer = round(sell_price * tax, 2)
                window_taxes['result'].update(answer)

            except Exception as e:
                sg.Popup(f'Error {e} detected')

    window_taxes.close()
