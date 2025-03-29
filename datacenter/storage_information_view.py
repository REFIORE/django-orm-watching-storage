from datacenter.functions import get_duration, format_duration
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_leaved_visits = Visit.objects.filter(leaved_at=None)
    non_closed_visits = []

    for visit in non_leaved_visits:
        duration = get_duration(visit)
        enter_localtime = localtime(visit.entered_at)
        visit_time = format_duration(duration)
        person = visit.passcard
        
        non_closed_visits.append(
            {
                'who_entered': person,
                'entered_at': enter_localtime,
                'duration': visit_time,
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
