import requests


if __name__ == '__main__':
    response = requests.post(
        'http://127.0.0.1:5000/insert/Pessoa/1983-01-13',
    )
    print(response)