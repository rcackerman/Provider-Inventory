"""
views.py

URL route handlers

Note that any handler params must match the URL route params.
For example the *say_hello* handler, handling the URL route '/hello/<username>',
  must be passed *username* as the argument.

"""


from google.appengine.api import users
from google.appengine.runtime.apiproxy_errors import CapabilityDisabledError
from google.appengine.ext import db


from flask import render_template, flash, url_for, redirect, request, make_response

from models import ExampleModel, Providers
from decorators import login_required, admin_required
from forms import ExampleForm, ProviderForm

def home():
	pass
	
def list_provs():
	providers = []
	provs = Providers.all()
	for prov in provs:
		if prov.pAgency in providers:
			pass
		else:
			providers.append(prov.pAgency)
	return render_template('providers.html', providers=providers)
	
	
def list_addresses(agency):
	addrs = []
	addresses = db.Query(Providers).filter('pAgency =', agency).order('pAddress')
	for addr in addresses:
		addrs.append((addr.pAddress, addr.programName))
	grouped_addrs = {}
	for elt in addrs: 
		if elt[0] in grouped_addrs:
			grouped_addrs[elt[0]].append(elt[1])
		else:
			grouped_addrs[elt[0]] = [elt[1]]
	return grouped_addrs

def add_notes(agency):
	form = ProviderForm(request.args)
	if form.validate_on_submit():
 		notes = ProviderNotes(
 			provider_name = form.providerName.data,
 			provider_notes = form.providerNote.data)
 		try:
 			notes.put()
 			flash(u'Example successfully saved.', 'success')
 			return redirect(url_for('list_provs'))
 		except:
	 		return redirect(url_for('list_provs'))
	return render_template('provider_notes.html', form=form, grouped_addrs=list_addresses(agency), pname=agency)


def warmup():
	"""App Engine warmup handler
	See http://code.google.com/appengine/docs/python/config/appconfig.html#Warming_Requests

	"""
	return ''

