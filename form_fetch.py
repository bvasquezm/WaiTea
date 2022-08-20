# Returns all rows from the first Sheet.
from sheet2api import Sheet2APIClient
import requests

URL = 'https://sheet2api.com/v1/YO89fUcHT26i/form-de-testeo'

user='persona_1'
query_params = {
    'limit': 10,
    'query_type': 'and',
    'usuario instagram': user,
}

client = Sheet2APIClient(api_url=URL)

response = client.get_rows(
    query=query_params,
)

print(response)

# Same as above, but using the requests.

'''
    headers = {'content-type': 'application/json'}
    response = requests.get(
        url=URL, headers=headers, params=query_params
    )

    print(response.json())
'''