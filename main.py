import re
from datetime import datetime

regex = re.compile(r"""
                   (?P<day>0[1-9]|[12]\d|3[01])    # Day: 01–31
                   /
                   (?P<month>0[1-9]|1[0-2])        # Month: 01–12
                   /
                   (?P<year>[12]\d{3})             # Year: 1000–2999
                  """, re.VERBOSE)

date_str = "31/12/2025"

match_obj = regex.fullmatch(date_str)

if match_obj:
    day = int(match_obj.group("day"))
    month = int(match_obj.group("month"))
    year = int(match_obj.group("year"))

    try:
        test_date = datetime(year, month, day)
        print(f"{date_str} is a valid date!")
    except ValueError:
        print(f"{date_str} is an invalid date!")
else:
    print(f"{date_str} is in the incorrect format.")
