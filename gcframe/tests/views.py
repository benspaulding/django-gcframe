# -*- coding: utf-8 -*-

""" Simple views for use in testing the gcframe app. """

from __future__ import unicode_literals

from django.http import HttpResponse

from gcframe.decorators import gcframe, gcframe_exempt


def normal(request):
    return HttpResponse('Plain, undecorated response.')

@gcframe()
def framed(request):
    return HttpResponse('GCFramed by a decorator.')

@gcframe_exempt
def exempt(request):
    return HttpResponse('Exempt from GCFraming.')
