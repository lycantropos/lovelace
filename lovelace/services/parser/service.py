from typing import (Iterator,
                    List)

from lovelace.utils import lines_generator


def parse_page_sections_names(content: str
                              ) -> List[str]:
    content_lines = lines_generator(content)
    sections_lines = filter(is_section_line, content_lines)
    return [line.strip(' =') for line in sections_lines]


def is_section_line(line: str) -> bool:
    section_line_head, section_line_tail = '== ', ' =='
    return (line.startswith(section_line_head) and
            line.endswith(section_line_tail))


def parse_page_section_content_lines(section_name: str,
                                     content: str
                                     ) -> Iterator[str]:
    section_line = f'== {section_name} =='
    content_lines = lines_generator(content)
    next(line for line in content_lines if line == section_line)
    for line in content_lines:
        line_is_section = is_section_line(line)
        if line_is_section:
            return
        yield line
