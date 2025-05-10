import re

date_str = "31/12/2025"

regex = re.compile(r"""
                   (?P<day>0[1-9]|[12]\d|3[01])    # Day: 01–31
                   /
                   (?P<month>0[1-9]|1[0-2])        # Month: 01–12
                   /
                   (?P<year>[12]\d{3})             # Year: 1000–2999
                  """, re.VERBOSE)


match_obj = regex.search(date_str)
match = match_obj.group() if match_obj else "No date found!"
day, month, year = match_obj.groups() if match_obj else "No date found!"
# day = match_obj.group("day") if match_obj else "No date found!"
# month = match_obj.group("month") if match_obj else "No date found!"
# year = match_obj.group("year") if match_obj else "No date found!"

print(f"Date: {match}")
print(f"Day: {day}")
print(f"Month: {month}")
print(f"Year: {year}")
