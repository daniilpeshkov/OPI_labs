import requests
import time


def get_usd_exchange():
    data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()
    return data['Valute']['USD']['Value']

def main():
    print('Курс доллара:', get_usd_exchange() )


if __name__ == '__main__':
    main()
