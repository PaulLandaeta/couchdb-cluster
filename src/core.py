from clients import store_clients
from movies import store_movies
from copies import store_copies
from rental import store_retanls
from prices import store_prices


def run():
    store_clients()
    store_movies()
    store_copies()
    store_retanls()
    store_prices()


if __name__ == '__main__':
    run()
