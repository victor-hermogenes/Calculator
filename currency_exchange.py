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
        [sg.Button('Back')]
    ]

    window = sg.Window('Currency Exchange', layout_currency, location=(680, 0))

    while True:
        event, values = window.read()

        if event == 'Back' or event == sg.WIN_CLOSED:
            break
        elif event == 'Choose Currency':
            try:
                exchange = float(get_exchange_rate(values['base'], values['target']))
                product_price_value = round(float(values['cost']), 2)
                product_price = round(product_price_value * exchange, 2)
                window['result'].update(exchange)
                window['result_product'].update(product_price)
            except Exception as e:
                print("Error occurred:", e)

    window.close()


