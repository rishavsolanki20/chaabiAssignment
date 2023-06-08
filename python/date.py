from datetime import date

def date_difference(from_date: str, to_date: str, difference: int) -> bool:
    year_from, month_from, day_from = map(int, from_date.split('-'))
    year_to, month_to, day_to = map(int, to_date.split('-'))
    from_date = date(year_from, month_from, day_from)
    to_date = date(year_to, month_to, day_to)
    delta = abs((from_date - to_date).days)
    return delta < difference

result = date_difference('22-01-01', '22-01-05', 4)
print(result) 
