import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from SSBRequester import ssbRequest
from jinja2 import Environment
import subprocess
from ckan.controllers.package import PackageController

def test():
	subprocess.call("query.sh")
	return "hello world"

def show_query_form(url):
	query = '''{
	  "query": [
	    {
	      "code": "Region",
	      "selection": {
		"filter": "item",
		"values": [
		  "1103"
		]
	      }
	    }
	  ],
	  "response": {
	    "format": "json-stat"
	  }
	}'''

	response = ssbRequest(url, query)
	
	return response

class NewSSBResource(PackageController):
	resource_form = 'custom_resource_form.html'

class ssbRetriever(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.ITemplateHelpers)
    plugins.implements(IRoutes, inherit=True)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
	toolkit.add_resource('templates/js','js')

    def get_helpers(self):
	return {'ssbRetriever_test':test,
	'ssbRetriever_show_query': show_query_form,
	}
   
    def before_map(self, map):
	map.connect('/dataset/new_ssb_resource',
	    controller='ckanext.ssbRetriever.controllers.SSBNewController:ResourceNew',
	    action='new')
	map.connect('/dataset/edit{id}',
	    controller='ckanext.ssbRetriever.controllers.SSBNewController:ResourceNew',
	    action='edit')
	return  map

    def after_map(self, map):
       return map
