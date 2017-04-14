from contextlib import contextmanager
from typing import Tuple, Dict, Any, Optional

from lovelace.utils import join_str


@contextmanager
def wrap_query_errors(
        *errors: Tuple[Exception, ...],
        **kwargs: Dict[str, Any]):
    try:
        yield
    except errors as err:
        kwargs_str = join_str(f'{key} {join_str(value)}'
                              for key, value in kwargs.items())
        err_msg = (f'Error while querying pages '
                   f'with {kwargs_str}.')
        raise IOError(err_msg) from err


def get_page_id(page_info: Dict[str, Any]
                ) -> Optional[str]:
    try:
        return page_info['pageid']
    except KeyError:
        return None


def get_title(page_info: Dict[str, Any]
              ) -> Optional[str]:
    try:
        return page_info['title']
    except KeyError:
        return None
