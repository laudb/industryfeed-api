import requests


def fetch_data(request_url=None):
    """
    A handler for fetching data from APIs.
    """

    try:
        response = requests.get(request_url)
        return response.json()
    except Exception as e:
        print({"message": "Could not return response"})
