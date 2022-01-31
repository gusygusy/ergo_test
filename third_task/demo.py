from currency_getter.objects_keeper import GetCurrencyData
from data.link_storage import uri

if __name__ == "__main__":

    g = GetCurrencyData()
    for _ in range(5):
        g.get_data(uri)