# Match the decimal in “ Hello your score is 2.9” using regular expression

import re

text = "Hello your score is 33.2"
match = re.search(r'\b\d+\.\d+\b', text)

if match:
    print(match.group())
