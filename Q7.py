# Match the digit and non Digit using regular expression

import re

text = "hello I am Sanika Bhoyar my ccat rank is 2202, my phone no. 8779688500!"


digit_matches = re.findall(r'\d', text)
print("Digits found:", digit_matches)


non_digit_matches = re.findall(r'\D', text)
print("Non-digits found:", non_digit_matches)
