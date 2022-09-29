import re

from utils import regex_unit_test


regex = r"""
    (?P<protocol>
        (http://)|
        (https://)
    )?
    (?P<domain>
        [a-zA-Z0-9\-_.]{1,255}
    )
    \.
    (?P<top_level_domain>
        [a-zA-Z0-9\-_]{1,63}
    )
    (?P<port>
        :[0-9]{1,65535}
    )?
    (?P<path>
        /[a-zA-Z0-9\-@:%_+.~#?&/=]*
    )?
"""

re_obj = re.compile(regex, re.VERBOSE)

if __name__ == "__main__":
    regex_unit_test("data/url_test.json", re_obj)