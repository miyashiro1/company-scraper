import json
import requests


def create_file():

    cookies = {
        'locale': 'fr',
        'axeptio_cookies': f"{'%22{$token%22:%223nk7cugeyxg6c69343ezsw%22%2C%22$$date%22:%222022-10-07T14:37:15.490Z%22%2C%22$$completed%22:false}'}",
        'axeptio_authorized_vendors': '%2C%2C',
        'axeptio_all_vendors': '%2C%2C',
    }

    headers = {
        'authority': 'www.free-work.com',
        'accept': 'application/ld+json',
        'accept-language': 'fr',
        # Requests sorts cookies= alphabetically
        # 'cookie': f"locale=fr; axeptio_cookies={%22{$token%22:%223nk7cugeyxg6c69343ezsw%22%2C%22$$date%22:%222022-10-07T14:37:15.490Z%22%2C%22$$completed%22:false};} axeptio_authorized_vendors=%2C%2C; axeptio_all_vendors=%2C%2C",
        'if-none-match': '"09391f9201ddedac8244e2c5de45aee4"',
        'referer': 'https://www.free-work.com/fr/companies?page=2',
        'sec-ch-ua': '"Chromium";v="106", "Google Chrome";v="106", "Not;A=Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sentry-trace': 'ecbd458b7cbb4d29a6ed9c198202ea7f-80bfd384f2a2097f-0',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
        'x-requested-with': 'XMLHttpRequest',
        'x-varnish-public': '1',
    }

    params = {
        'itemsPerPage': '669',
        'page': '1',
        'directoryFreeWork': 'true',
        'order[date]': 'desc',
    }

    url = r'https://www.free-work.com/fr/companies/'

    response = requests.get('https://www.free-work.com/api/companies', params=params, cookies=cookies, headers=headers)
    data = response.json()

    # Creating a json file so i don't need to request the website multiple times.
    with open('data.json', 'a') as f:
        json.dump(data, f)



