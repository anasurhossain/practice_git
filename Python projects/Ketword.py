"""
Keyword Argument
"""
def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"
phone_num = get_phone(country=61, first=158, area=90, last=284)
print(phone_num)
