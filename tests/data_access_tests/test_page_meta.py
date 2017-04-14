import pytest

from lovelace.services.data_access import (fetch_pages_ids,
                                           fetch_titles)
from tests.strategies import (MIN_PAGE_ID,
                              MAX_PAGE_ID)


def test_fetch_titles(page_id: str,
                      invalid_page_id: str) -> None:
    fetched_title, = fetch_titles(page_id)
    assert fetched_title is None or isinstance(fetched_title, str)
    with pytest.raises(IOError):
        next(fetch_titles(invalid_page_id))


def test_parse_page_id(title: str,
                       invalid_title: str) -> None:
    page_id, = fetch_pages_ids(title)
    assert (page_id is None or
            MIN_PAGE_ID < int(page_id) < MAX_PAGE_ID)
    with pytest.raises(IOError):
        next(fetch_titles(invalid_title))
