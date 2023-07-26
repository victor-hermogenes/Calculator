import requests


def get_exchange_rate(base_currency, target_currency):
    try:
        response = requests.get(f'https://economia.awesomeapi.com.br/last/{base_currency}-{target_currency}')
        data = response.json()
        return data[f'{base_currency}{target_currency}']['bid']

    except ValueError:
        return None
