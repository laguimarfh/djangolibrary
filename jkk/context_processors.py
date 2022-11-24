from django.db.models import Count
from . import models
import datetime


def base_context(request):
    process_s8 = models.Jkks8.objects.all().order_by('created')
    elementsS8 = models.s8elements.objects.all()
    # check = models.checkJkk.objects.all()
    # period = models.periodJkk.objects.all().order_by('-created')
    # elements = models.checkJkk.objects.all()
    # stopw = models.stopwatch.objects.all()
    # check2 = models.checkJkk.objects.get(pk=1)
    # coord = models.AjaxImage.objects.all()
    # side = models.Sheet.objects.all()[:1]
    # today = datetime.datetime.today().date()
    # number_defects_day = models.Sheet.objects.filter(created__date=today).count()

    return {
        'process_s8': process_s8,
        'elementsS8': elementsS8,
    }

