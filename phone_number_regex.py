from utils import regex_unit_test


"""
A complete phone number includes the below components:
[country_code][area_code][prefix][line_number]
A valid phone number will have some rules:
- [country_code] (optional): are two digits with a plus sign (optional) and
                             parentheses (optional)
- [area_code]: are three or two digits and parentheses (optional)
- [prefix]: are three digits
- [line_number]: are four digits
- when country-code separator is None, other separator is also None
- when area-prefix separator is dot (.) or hyphen (-), prefix-line separator is
  the same
- when area-prefix separator is whitespace, prefix-line separator can be any type
"""


regex = r"""
    (?P<country_code>
        (?P<has_parentheses_c>\()?  # check if having opening parenthesis
        \+?\d{2}                    # two digits country code 
        (?(has_parentheses_c)\)|)   # if having, add closing parenthesis
    )?
    # If country_code separator is None, then other separator is None too
    (?P<has_whitespace>\s)?         
    (?P<area_code>
        (?P<has_parentheses_a>\()?  
        \d{2,3}   # two or three digits area code
        (?(has_parentheses_a)\)|)     
    )
    (?(has_whitespace)              
        (?P<area_prefix_separator>[\.\-])?  
        (?P<area_prefix_whitespace_separator>\s)?|
    )
    (?P<prefix>
        \d{3}  # three digits prefix                     
    )
    (?(has_whitespace)
        # if area-prefix separator is not whitespace 
        # then prefix-line separator is the same  
        # else if area-prefix separator is whitespace  
        # then prefix-line separator can be any types
        (?(area_prefix_separator)   
            (?P=area_prefix_separator)|
            (?(area_prefix_whitespace_separator)    
                [\.\-\s]?|
            )
        )|
    )   
    (?P<line_number>
        \d{4}   # four digits line number 
    )
"""


if __name__ == "__main__":
    regex_unit_test("data/phone_number_test.json", regex)
