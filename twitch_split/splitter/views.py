from django.shortcuts import render
from splitter import lib

# Create your views here.

def one_full(request, param_username):
	page_vars = { 'page_title': 'Single Stream View' }
	streams = { param_username: lib.validate_streams([param_username]) }
	page_vars['height'] = "100%"
	page_vars['width'] = "100%"
	page_vars['channel'] = param_username

	return render(request, "one_full.html", page_vars)
