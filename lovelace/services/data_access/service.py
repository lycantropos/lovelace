from typing import (Any,
                    Optional,
                    Iterator,
                    Dict,
                    Tuple)

import requests

from lovelace.config import API_URL
from lovelace.utils import join_str
from lovelace.services.parser.utils import (wrap_query_errors,
                                            get_page_id,
                                            get_title)


def query_wikipedia_api(**params: Dict[str, str]
                        ) -> Dict[str, Any]:
    params['format'] = 'json'
    params['action'] = 'query'
    response = requests.get(API_URL,
                            params=params)
    return response.json()


def fetch_pages_contents(*pages_ids: Tuple[str, ...]
                         ) -> Iterator[Optional[str]]:
    params = dict(prop='extracts',
                  explaintext='',
                  rvprop='ids',
                  pageids=join_str(pages_ids,
                                   sep='|'))
    response = query_wikipedia_api(**params)
    query = response['query']
    pages_info = query['pages']
    for page_id in pages_ids:
        page_info = pages_info[page_id]
        try:
            yield page_info['extract']
        except KeyError:
            yield None


def search_page_title(title_part: str,
                      results_count: int = 10
                      ) -> Iterator[str]:
    params = dict(list='search',
                  srprop='',
                  srlimit=results_count,
                  limit=results_count,
                  srsearch=title_part)

    response = query_wikipedia_api(**params)
    validate_response(response)

    with wrap_query_errors(KeyError,
                           title_part=title_part):
        query = response['query']
        results = query['search']

    for result in results:
        yield result['title']


def validate_response(response: Dict[str, Any]
                      ) -> None:
    errors_messages = response.get('error')
    if errors_messages is None:
        return
    errors_messages_info = errors_messages['info']
    raise IOError(errors_messages_info)


def fetch_pages_ids(*titles: Tuple[str, ...]
                    ) -> Iterator[Optional[str]]:
    params = dict(prop='info',
                  titles=join_str(titles,
                                  sep='|'))

    response = query_wikipedia_api(**params)

    with wrap_query_errors(KeyError,
                           titles=titles):
        query = response['query']
        pages_info = query['pages']

    with wrap_query_errors(AttributeError,
                           titles=titles):
        return map(get_page_id, pages_info.values())


def fetch_titles(*pages_ids: Tuple[str, ...]
                 ) -> Iterator[Optional[str]]:
    params = dict(prop='info',
                  pageids=join_str(pages_ids,
                                   sep='|'))

    response = query_wikipedia_api(**params)

    with wrap_query_errors(KeyError,
                           pages_ids=pages_ids):
        query = response['query']
        pages_info = query['pages']

    with wrap_query_errors(AttributeError,
                           pages_ids=pages_ids):
        return map(get_title, pages_info.values())
