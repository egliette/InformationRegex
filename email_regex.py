import re

from utils import regex_unit_test


regex = r"""
    (?P<username>
        [a-zA-Z0-9\-_.]{1,63}
    )
    @
    (?P<domain>
        [a-zA-Z0-9\-_.]{1,255}
    )
    \.
    (?P<top_level_domain>
        [a-zA-Z0-9\-_]{1,63}
    )
"""

re_obj = re.compile(regex, re.VERBOSE)

if __name__ == "__main__":
    regex_unit_test("data/email_test.json", re_obj)
