import re

date_str = "21/12/2025"

regex = re.compile(r"""
                   (0([1-9])|1(\d)|2(\d)|3([01])){1}   # DD
                   /
                   (0([1-9])|1([0-2])){1}              # MM
                   /
                   [12]{1}\d{3}                        # YYYY
                  """, re.VERBOSE)


match_obj = regex.search(date_str)
match = match_obj.group() if match_obj else "No date found!"

print(f"Date: {match}")
