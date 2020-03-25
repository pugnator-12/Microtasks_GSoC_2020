import requests

GROUPSIO_API_URL = 'https://groups.io/api/v1/'
LOGIN = 'login'
GET = 'get'
POST = 'post'
GET_SUBSCRIPTIONS = 'getsubs'
GET_PERMISSIONS = 'getperms'
PER_PAGE = 100

session = requests.Session()


def urijoin(*args):
    """Joins given arguments into a URI.

    :returns: a URI string
    """
    return '/'.join(map(lambda x: str(x).strip('/'), args))


def fetch(url, payload, method=GET):
    """Fetch requests from groupsio API"""

    if method == POST:
        r = session.post(url, data=payload)
    else:
        r = session.get(url, params=payload)
    try:
        r.raise_for_status()
    except requests.exceptions.HTTPError as e:
        raise e

    return r


def get_download_permission(group, login=False, email='xxxx', password='xxx'):
    if login:
        payload = {
            'email': email,
            'password': password
        }

        url = urijoin(GROUPSIO_API_URL, LOGIN)
        fetch(url, payload, method=POST)

    url = urijoin(GROUPSIO_API_URL, GET_PERMISSIONS)

    keep_fetching = True
    payload = {
        "group_name": group,
    }

    r = fetch(url, payload)
    response_raw = r.json()
    return response_raw['download_archives']


def get_subscriptions(email, password):
    payload = {
        'email': email,
        'password': password
    }

    url = urijoin(GROUPSIO_API_URL, LOGIN)
    fetch(url, payload, method=POST)

    url = urijoin(GROUPSIO_API_URL, GET_SUBSCRIPTIONS)

    keep_fetching = True
    payload = {
        "limit": PER_PAGE
    }

    while keep_fetching:
        r = fetch(url, payload)
        response_raw = r.json()
        subscriptions = response_raw['data']

        for sub in subscriptions:
            print(sub['group_name'] + ' , download archives: ' + str(get_download_permission(group=sub['group_name'])))

        payload['page_token'] = response_raw['next_page_token']
        keep_fetching = response_raw['has_more']


def main():
    groups_io_email = input('Enter your email: ')
    groups_io_password = input('Enter your password: ')
    print("***** ***** ***** *****")
    get_subscriptions(groups_io_email, groups_io_password)


if __name__ == "__main__":
    main()
