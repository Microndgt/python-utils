import datetime
from dateutil.relativedelta import relativedelta


def get_datetime_delta(now_day=None, years=0, months=0, weeks=0, days=0, hours=0, minutes=0, seconds=0):
    '''
    获取一个增量后的日期

    >>> now = datetime.datetime(2017, 5, 15, 15, 47, 23)
    >>> get_datetime_delta(now)
    datetime.datetime(2017, 5, 15, 15, 47, 23)
    >>> get_datetime_delta(now, years=1)
    datetime.datetime(2018, 5, 15, 15, 47, 23)
    >>> get_datetime_delta(now, years=-1)
    datetime.datetime(2016, 5, 15, 15, 47, 23)
    >>> get_datetime_delta(now, years=1, months=1)
    datetime.datetime(2018, 6, 15, 15, 47, 23)
    >>> get_datetime_delta(now, years=1, months=1, weeks=1)
    datetime.datetime(2018, 6, 22, 15, 47, 23)
    >>> get_datetime_delta(now, years=1, months=1, weeks=1, days=1)
    datetime.datetime(2018, 6, 23, 15, 47, 23)
    >>> get_datetime_delta(now, years=1, months=1, weeks=1, days=1, hours=1)
    datetime.datetime(2018, 6, 23, 16, 47, 23)
    >>> get_datetime_delta(now, years=1, months=1, weeks=1, days=1, hours=1, minutes=1, seconds=1)
    datetime.datetime(2018, 6, 23, 16, 48, 24)
    >>> get_datetime_delta(now, days=-1, hours=1)
    datetime.datetime(2017, 5, 14, 16, 47, 23)
    '''
    if not years and not months and not weeks and not days and not hours and not minutes and not seconds:
        return now_day
    if now_day is None:
        now_day = datetime.datetime.now()
    if years or months:
        now_day = now_day + relativedelta(years=years, months=months)

    now_day = now_day + datetime.timedelta(weeks=weeks, days=days, hours=hours, minutes=minutes, seconds=seconds)

    return now_day

