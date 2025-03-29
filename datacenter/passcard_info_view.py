from datacenter.functions import get_duration, format_duration
from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime
from django.shortcuts import get_object_or_404


def passcard_info_view(request, passcode):
    passcard = get_object_or_404(Passcard, passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in passcard_visits:
        duration = get_duration(visit)
        enter_localtime = localtime(visit.entered_at)
        visit_time = format_duration(duration)

        this_passcard_visits.append(
            {
                'entered_at': enter_localtime,
                'duration': visit_time,
                'is_strange': False
            },
        )
    context = {
        'passcard': passcard,
        'this_passcard_visits': this_passcard_visits
    }
    return render(request, 'passcard_info.html', context)
