import re
import string

from lovelace.services.data_access import fetch_pages_contents


def test_fetch_page_content(page_id: str) -> None:
    page_content, = fetch_pages_contents(page_id)

    if not page_content:
        return

    page_content_without_whitespaces = re.sub(pattern=r'\s',
                                              repl='',
                                              string=page_content)
    latin_alphanumeric_characters = string.ascii_letters + string.digits
    latin_alphanumeric_characters_count = sum(
        character in latin_alphanumeric_characters
        for character in page_content_without_whitespaces)
    latin_alphanumeric_characters_frequency = (
        latin_alphanumeric_characters_count
        / len(page_content_without_whitespaces))

    min_latin_alphanumeric_symbols_frequency = 0.5

    assert (latin_alphanumeric_characters_frequency == 0 or
            latin_alphanumeric_characters_frequency
            >= min_latin_alphanumeric_symbols_frequency)
