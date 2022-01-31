import datetime
import requests


class CacheCurrencyData:

    def __init__(self):
        self.cache_data = None

    def set_cache(self, data):
        self.cache_data = data
        print(f'currency value has been set...')
        return True

    def get_cache(self):
        print('taking from cache...')
        return self.cache_data


class TimeDelay:

    def __init__(self):
        self._started_at = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

    def __call__(self):
        time_passed = datetime.datetime.now() - self._started_at

        if time_passed.total_seconds() > 0.05:
            self._started_at = datetime.datetime.now()
            return True

        elif time_passed.total_seconds() == 0:
            self._started_at = datetime.datetime.now()
            return True

        self._started_at = datetime.datetime.now()
        return False


class GetCurrencyData:

    def __init__(self):
        self.cache_currency_data = CacheCurrencyData()
        self.time = TimeDelay()
        self.cache_currency_data_methods = [m for m in dir(CacheCurrencyData) if not m.startswith('_')]
        self.time_delay_methods = [m for m in dir(TimeDelay) if not m.startswith('_')]

    def __getattr__(self, func):

        def method(*args):
            if func in self.cache_currency_data_methods:
                return getattr(self.cache_currency_data, func)(*args)

            elif func in self.time_delay_methods:
                return getattr(self.time_delay_methods, func)(*args)

            else:
                raise AttributeError

        return method

    def get_data(self, url):
        if self.time():
            response = requests.get(url)
            resp_dict = self._xml_to_dict(response.text)
            exact_data = self._get_exact_data(resp_dict)
            self.cache_currency_data.set_cache(exact_data)
            return exact_data
        else:
            return self.cache_currency_data.get_cache()

    @staticmethod
    def _xml_to_dict(data):
        import xmltodict
        data = xmltodict.parse(data)
        return data

    @staticmethod
    def _get_exact_data(data):
        data = data['ValCurs']['Valute']
        usd_data = [i for i in data if i['NumCode'] == '840']
        eu_data = [i for i in data if i['NumCode'] == '978']

        dt = {data['CharCode']: round(float(data['Value'].replace(',', '.')), 2) for data in usd_data}
        d = {data['CharCode']: round(float(data['Value'].replace(',', '.')), 2) for data in eu_data}
        final_dict = {**dt, **d}

        for k, v in final_dict.items():
            final_dict[k] = f"Decimal {v}"

        return final_dict
