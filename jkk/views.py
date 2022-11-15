from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, DetailView, ListView
from jkk.forms import dailyjkkForm, periodjkkForm, stopwatchForm
from . import models
from datetime import datetime
# Create your views here.


# class JkkView(CreateView):
#     """
#     The CS homepage
#     """
#     form_class = jkkForm
#     template_name = 'jkk/stopwatch.html'
#     def get_context_data(self, **kwargs):
#         jkk_form = jkkForm
#         context = super().get_context_data(**kwargs)
#         context['jkk_form'] = jkk_form
        
#         return context

class dailyjkkView(CreateView):
    """
    The JKK Homepage
    """
    form_class = dailyjkkForm
    template_name = 'jkk/home.html'

    def get_context_data(self, **kwargs):
        dailyjkk_form = dailyjkkForm
        context = super().get_context_data(**kwargs)
        context['dailyjkk_form'] = dailyjkk_form
        
        return context


class periodjkkView(DetailView, CreateView):
    """
    The JKK Homepage
    """
    model = models.dailyJkk
    form_class = periodjkkForm
    template_name = 'jkk/jkkperiod.html'
    context_object_name = 'dailyjkk'
    
    # def get_queryset(self):
    #     return models.dailyJkk.objects.fi

    def get_context_data(self, **kwargs):
        periodjkk_form = periodjkkForm
        context = super().get_context_data(**kwargs)
        context['periodjkk_form'] = periodjkk_form
        
        return context

# class checkjkkView(DetailView, CreateView):
#     """
#     The JKK Homepage
#     """
#     model = models.checkJkk
#     form_class = checkjkkForm
#     template_name = 'jkk/jkkcheck.html'
#     context_object_name = 'checkjkk'
    
#     # def get_queryset(self):
#     #     return models.dailyJkk.objects.fi

#     def get_context_data(self, **kwargs):
#         periodjkk_form = periodjkkForm
#         context = super().get_context_data(**kwargs)
#         context['periodjkk_form'] = periodjkk_form
        
#         return context

class stopwatchView(CreateView):
    """
    The JKK Homepage
    """
    model = models.stopwatch
    form_class = stopwatchForm
    template_name = 'jkk/stopwatch.html'
    # context_object_name = 'stopwatch'
    
    # def get_queryset(self):
    #     return models.dailyJkk.objects.fi

    def get_context_data(self, **kwargs):
        stopwatch_form = stopwatchForm
        context = super().get_context_data(**kwargs)
        context['stopwatch_form'] = stopwatch_form
        
        return context
