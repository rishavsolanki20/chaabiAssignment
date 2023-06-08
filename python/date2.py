from datetime import datetime, timedelta

def subtract_days(date: str, n: int) -> str:
    date_format = '%y-%m-%d'
    date = datetime.strptime(date, date_format)
    new_date = date - timedelta(days=n)
    return new_date.strftime(date_format)

result = subtract_days('16-12-10', 11)
print(result)
