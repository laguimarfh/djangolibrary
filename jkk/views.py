from django.shortcuts import render

from django.views.generic import TemplateView, CreateView, DetailView, ListView
from jkk.forms import jkks8Form
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


class jkkhomeView(TemplateView):
    """
    The JKK S8 PROCESS
    """
    template_name = 'jkk/home.html'
    

    # def get_context_data(self, **kwargs):
    #     jkks8_form = jkks8Form
    #     context = super().get_context_data(**kwargs)
    #     context['jkks8_form'] = jkks8_form
        
    #     return context




class jkks8View(CreateView):
    """
    The JKK S8 PROCESS
    """
    form_class = jkks8Form
    template_name = 'jkk/jkks8.html'

    def get_context_data(self, **kwargs):
        jkks8_form = jkks8Form
        context = super().get_context_data(**kwargs)
        context['jkks8_form'] = jkks8_form
        return context


# class periodjkkView(DetailView, CreateView):
#     """
#     The JKK Homepage
#     """
#     model = models.Jkk
#     form_class = periodjkkForm
#     template_name = 'jkk/jkkperiod.html'
#     context_object_name = 'jkk'
    
    # def get_queryset(self):
    #     return models.dailyJkk.objects.fi

#     def get_context_data(self, **kwargs):
#         periodjkk_form = periodjkkForm
#         context = super().get_context_data(**kwargs)
#         context['periodjkk_form'] = periodjkk_form
        
#         return context


# class stopwatchView(CreateView):
#     """
#     The JKK Homepage
#     """
#     model = models.stopwatch
#     form_class = stopwatchForm
#     template_name = 'jkk/stopwatch.html'
#     # context_object_name = 'stopwatch'
    
#     # def get_queryset(self):
    #     return models.dailyJkk.objects.fi

    # def get_context_data(self, **kwargs):
    #     stopwatch_form = stopwatchForm
    #     context = super().get_context_data(**kwargs)
    #     context['stopwatch_form'] = stopwatch_form
        
    #     return context
