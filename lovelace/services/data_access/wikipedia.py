from typing import Dict, Any

import requests

from lovelace.config import API_URL


def query_wikipedia_api(**params: Dict[str, str]
                        ) -> Dict[str, Any]:
    params['format'] = 'json'
    params['action'] = 'query'
    response = requests.get(API_URL,
                            params=params)
    return response.json()
