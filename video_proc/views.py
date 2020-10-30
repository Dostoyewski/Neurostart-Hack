from django.shortcuts import render, get_object_or_404
from .models import Competition, CompetitionRecording
from .serializers import CompetitionRecordingSerializer, CompetitionSerializer
from django.contrib.auth.decorators import login_required
from .forms import CompetitionRecordingForm
from django.http import HttpResponseRedirect
from django.urls import reverse


@login_required()
def video_recording(request, slug):
    """
    This function return video page
    :param request:
    :param slug: slug to UProfile
    :return: render
    """
    print(slug)
    v_profile = get_object_or_404(Competition, slug=slug)
    if request.method == 'POST':
        form = CompetitionRecordingForm(request.POST, request.FILES)
        if form.is_valid():
            recording = CompetitionRecording()
            recording.video = form.cleaned_data['video']
            recording.user = request.user
            recording.competition = v_profile
            recording.save()
            return HttpResponseRedirect(reverse('competition_list'))

    else:
        form = CompetitionRecordingForm()
    return render(request, 'competition_detail.html', {'comp_profile': v_profile,
                                                       'form': form,
                                                       'absolute': reverse('video_rec', args=(v_profile.slug, ))})


def competitions_list(request):
    """
    Page with all competitions tasks
    :param request:
    :return:
    """
    return render(request, 'videos_home.html', {"recordings": CompetitionSerializer(Competition.objects.all(),
                                                                                    many=True).data})
