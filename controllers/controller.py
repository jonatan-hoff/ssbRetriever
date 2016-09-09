import logging
from urllib import urlencode
import datetime
import mimetypes
import cgi

from pylons import config
from paste.deploy.converters import asbool
import paste.fileapp

import ckan.logic as logic
import ckan.lib.base as base
import ckan.lib.maintain as maintain
import ckan.lib.i18n as i18n
import ckan.lib.navl.dictization_functions as dict_fns
import ckan.lib.helpers as h
import ckan.model as model
import ckan.lib.datapreview as datapreview
import ckan.lib.plugins
import ckan.lib.uploader as uploader
import ckan.plugins as p
import ckan.lib.render
import requests,json

from ckan.common import OrderedDict, _, json, request, c, g, response
from ckan.controllers.package import PackageController
from ckanext.ssbRetriever.utils import execute_query

log = logging.getLogger(__name__)

render = base.render
abort = base.abort
redirect = base.redirect

NotFound = logic.NotFound
NotAuthorized = logic.NotAuthorized
ValidationError = logic.ValidationError
check_access = logic.check_access
get_action = logic.get_action
tuplize_dict = logic.tuplize_dict
clean_dict = logic.clean_dict
parse_params = logic.parse_params
flatten_to_string_key = logic.flatten_to_string_key

lookup_package_plugin = ckan.lib.plugins.lookup_package_plugin

log = logging.getLogger(__name__)

class SSBController(PackageController):
    def new_resource(self, data=None, errors=None, error_summary=None):
	#check if metadada info exists and add it otherwise
	#context = {'model': model, 'session': model.Session, 'user': c.user or c.author}
	#package_info = get_action('package_show')(context, {'id': c.pkg.id})

        #data_dict = clean_dict(dict_fns.unflatten(tuplize_dict(parse_params(request.POST))))
	#pkg_dict = get_action('package_update')(context, data_dict)
	#id = pkg_dict['name']
	#data = data or clean_dict(dict_fns.unflatten(tuplize_dict(parse_params(request.POST))))
	#resource_id = data['id']
	#data['id'] = resource_id
	#data['package_id'] = id
	#get_action('resource_create')(context, data)

	#query_results = execute_query(request.params['id'], "http//:vg.no")
	#return render(query_results)
	#if 'resource-edit' in request.params:
	#	query_results = execute_query(request.params['query-text'], request.params['query-url'], self.packageendpoint)
	#	c.query = request.params['query-text']
	#	
	#	return query_results

	query = """ {
  "query": [
    {
      "code": "ArbeidsTid",
      "selection": {
        "filter": "item",
        "values": [
          "1103"
        ]
      }
    }
  ],
  "response": {
    "format": "csv"
  }
}
"""
	url="http://data.ssb.no/api/v0/no/table/08146"
	#headers = {'cache-control': 'no-cache'}
	ssbResponse = requests.get(url)
	
	#send string as file
	filesRequests ={'upload': ('ssbData.csv', ssbResponse.text)}
	filesCkan = [('upload', filesRequests)]
	
	headers = {"Authorization": "f65b83f5-c14a-4440-b07f-3be58acb686a"}	
	ckanurl = "http://localhost/api/action/resource_create"

	#note resource ID not actually needed
	params= {'description': 'ssb test', 'owner_org':'stavanger','package_id':'0123fadc-3a9c-4c4c-8392-c38132a136a8','name': "dataFraController", "url": " ", "id":"74bbb978-323c-4f82-9a27-77f1d2f1b663"}
	
	postResponse = requests.post(ckanurl, files = filesRequests, headers=headers, data = params)

	#return response
	log.warning("================CONTROLLER=====================")
	log.warning("response: " + postResponse.text)
	
	log.warning("================CONTROLLER=====================")

        return render('package/resources.html')



