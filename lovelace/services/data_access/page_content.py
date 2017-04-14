from typing import (Optional,
                    Iterator,
                    Tuple)

from lovelace.utils import join_str
from .wikipedia import query_wikipedia_api


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
