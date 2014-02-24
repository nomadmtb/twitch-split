from django.shortcuts import render
from splitter import lib
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.

def one_full(request, param_username):
	page_vars = { 'page_title': 'Single Stream View' }
	streams = { param_username: lib.validate_streams([param_username]) }
	page_vars['layout'] = "one_full"
	page_vars['channel'] = param_username

	return render(request, "one_full.html", page_vars)

def two_horiz(request, param_username_1, param_username_2):
	entered_streams = [param_username_1, param_username_2]
	page_vars = { 'page_title': 'Double View' }
	page_vars['streams'] = entered_streams

	if lib.validate_streams(entered_streams) == False:
		messages.add_message(request, messages.ERROR, 'ERROR: Invalid STREAM')
		return HttpResponseRedirect('/')


	orientation = request.GET.get('orientation', 'horizontal')

	if orientation == 'vertical':
		page_vars['layout'] = 'two_vert'
		return render(request, 'two_vert.html', page_vars)
	else:
		page_vars['layout'] = 'two_horiz'
		return render(request, 'two_horiz.html', page_vars)