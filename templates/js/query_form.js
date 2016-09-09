"use strict";

ckan.module('query_form', function($, _) {
    return {
        initialize: function() {

		$('#toggle-query').on('click', function(){
			$('#query-url').toggle();
			$('#query-text').toggle();
			//$('.image-upload').toggle();
			//$('#submitButton').toggle();
			//$('#submitButton').toggle();
			//$('#customSubmitButton').toggle();
			//console.log(this.options.url_type);
			//if(options.is_upload === true){
			//	options.is_upload = false;
			//} else {
			//	options.is_upload = true;
			//}
			//console.log("val: " + document.getElementById('field-image-url').innerHTML);
			//var url = document.getElementById('field-image-url');
			

			//var data = new Blob("hellow wold im blob", {type: 'text/plain'});
			//var textfile = window.URL.createObjectURL(data);

			//url.value = textfile;
		});

		var settings = {
			"async": true,
			"crossdomain": true,
			"url": document.getElementById('query-url').value,
			"method": "POST",
			"headers":{"cache-control": "no-cache", "Access-Control-Request-Headers":"x-requested-with"},
			"dataType": "jsonp",
			"data": document.getElementById('query-text').value
		}

		$('#run-query').on('click', function(){
			
			//var file_name = this.input.val().split(/^C:\\fakepath\\/).pop();
      			//this.field_url_input.val(file_name);
			settings.url = document.getElementById('query-url').value;
			console.log("url: ") + settings.url;
			console.log("query: ") + settings.data;
			//$('#submitButton').toggle();
			$.ajax(settings).done(function(response){
				for(d in JSON.parse(response)){
					
					console.log(d);
				}
			});
		});
        },

    };
});
