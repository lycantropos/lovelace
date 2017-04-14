from lovelace.services.data_access import search_page_title


def test_search_page_title(title: str) -> None:
    search_result = search_page_title(title_part=title)
    assert next(search_result)
