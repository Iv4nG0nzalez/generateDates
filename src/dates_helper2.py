import datetime

def get_default_date_data(initial_date: str, end_date:str, default_value:any) -> list:

    if initial_date is None: 
        return []
    start = datetime.datetime.strptime(initial_date, "%m/%d/%Y")

    end = datetime.datetime.strptime(end_date, "%m/%d/%Y")
    date_generated = [start + datetime.timedelta(days=x) for x in range(0, (end-start + datetime.timedelta(1)).days)]

    data_formated = []

    for date in date_generated:
        file_date = {}
        file_date['date'] = date.strftime("%-m/%d/%Y")
        file_date['participants'] = default_value
        data_formated.append(file_date)

    return data_formated




