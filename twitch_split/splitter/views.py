from django.shortcuts import render
from splitter import lib

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

	streams = lib.validate_streams(entered_streams)
	page_vars['layout'] = "two_horiz"
	page_vars['streams'] = entered_streams

	return render(request, "two_horiz.html", page_vars)