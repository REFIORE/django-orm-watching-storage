from django.utils import timezone


def get_duration(visit):
    entered_localtime = timezone.localtime(visit.entered_at)
    date_now = timezone.localtime(timezone.now())
    delta = date_now - entered_localtime
    return delta


def format_duration(duration):
    seconds = duration.seconds
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    sec = seconds % 60
    return f"{hours}:{minutes}:{sec}"