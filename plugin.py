import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
import requests

def query_form():
	return "the end is coming"

class ssbRetriever(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(p.ITemplateHelpers)

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')

    def get_helpers(self):
	return {'ssbRetriever_query_form': query_form}

