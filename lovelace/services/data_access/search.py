from typing import (Any,
                    Iterator,
                    Dict)

from .utils import wrap_query_errors
from .wikipedia import query_wikipedia_api


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
