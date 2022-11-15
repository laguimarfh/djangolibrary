from django.db.models import Count
from . import models
import datetime


def base_context(request):
    process = models.dailyJkk.objects.all()
    # elements = models.checkJkk.objects.all()
    stopw = models.stopwatch.objects.all()

    # coord = models.AjaxImage.objects.all()
    # side = models.Sheet.objects.all()[:1]
    # today = datetime.datetime.today().date()
    # number_defects_day = models.Sheet.objects.filter(created__date=today).count()

    return {
        'process': process,
        # 'elements': elements,
        'stopw': stopw,
    }

