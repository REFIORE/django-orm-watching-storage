from django.utils import timezone


def is_visit_long(duration, minutes=60):
    seconds = minutes*60
    long_visit = duration.total_seconds()>seconds
    return long_visit


def get_duration(visit):
    entered_localtime = timezone.localtime(visit.entered_at)
    date_now = timezone.localtime(timezone.now())
    delta = date_now - entered_localtime
    return delta


def format_duration(duration):
    seconds_in_hour = 3600
    minutes_in_hour = 60
    seconds_in_minute = 60
    seconds = duration.total_seconds()
    hours = seconds // seconds_in_hour
    minutes = (seconds % seconds_in_hour) // minutes_in_hour
    sec = seconds % seconds_in_minute
    return f"{hours}:{minutes}:{sec}"
