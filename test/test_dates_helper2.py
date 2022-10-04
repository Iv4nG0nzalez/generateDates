from src.dates_helper2 import get_default_date_data

def test_get_default_date_data_simple_element():
    start_date = '9/12/2022'
    end_date = '9/12/2022'
    default_value = -99999

    dates = get_default_date_data(start_date, end_date, default_value)
    assert {'date': '9/12/2022', 'participants': -99999} in dates


def test_get_default_date_data_in_interval_with_none():
    start_date = '9/12/2022'
    end_date = '9/15/2022'
    default_value = None

    dates = get_default_date_data(start_date, end_date, default_value)
    assert {'date': '9/12/2022', 'participants': None} in dates
    assert {'date': '9/13/2022', 'participants': None} in dates
    assert {'date': '9/14/2022', 'participants': None} in dates
    assert {'date': '9/15/2022', 'participants': None} in dates


def test_get_default_date_data_in_interval():
    start_date = '9/12/2022'
    end_date = '9/15/2022'
    default_value = -99999

    dates = get_default_date_data(start_date, end_date, default_value)
    assert {'date': '9/12/2022', 'participants': -99999} in dates
    assert {'date': '9/13/2022', 'participants': -99999} in dates
    assert {'date': '9/14/2022', 'participants': -99999} in dates
    assert {'date': '9/15/2022', 'participants': -99999} in dates


def test_get_default_date_data_in_interval_invalid_end_date():
    start_date = '9/15/2022'
    end_date = '9/10/2022'
    default_value = -99999

    dates = get_default_date_data(start_date, end_date, default_value)
    assert len(dates) == 0


def test_get_default_date_data_in_interval_none_arguments():
    start_date = None
    end_date = None
    default_value = -99999

    dates = get_default_date_data(start_date, end_date, default_value)
    assert len(dates) == 0


def test_get_default_date_data_in_interval_str_default_value():
    start_date = '9/12/2022'
    end_date = '9/15/2022'
    default_value = "0h 0m"

    dates = get_default_date_data(start_date, end_date, default_value)
    assert {'date': '9/12/2022', 'participants': '0h 0m'} in dates
    assert {'date': '9/13/2022', 'participants': '0h 0m'} in dates
    assert {'date': '9/14/2022', 'participants': '0h 0m'} in dates
    assert {'date': '9/15/2022', 'participants': '0h 0m'} in dates
