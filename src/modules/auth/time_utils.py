import datetime

from . import config


def get_tz() -> datetime.timezone:
    tz_offset_hours = config.UTC_OFFSET_HOURS
    tz_offset = datetime.timedelta(hours=tz_offset_hours)
    tz = datetime.timezone(tz_offset)
    return tz


def datetime_now_with_tz() -> datetime.datetime:
    tz = get_tz()
    dt = datetime.datetime.now(tz)
    return dt


def datetime_from_timestamp_with_tz(timestamp: int) -> datetime.datetime:
    tz = get_tz()
    dt = datetime.datetime.fromtimestamp(timestamp, tz)
    return dt
