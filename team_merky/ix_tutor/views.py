# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import S2STestForm, DSPUserForm


# Create your views here.
def index(request):
	#return HttpResponse("IX tutor app")
	if request.method == 'GET':
		template = loader.get_template('ix_tutor/index.html')
		context = {}
		#form = S2STestForm()
		#context['form'] = form
		return HttpResponse(template.render(context, request))




	#return HttpResponse("IX tutor app")

