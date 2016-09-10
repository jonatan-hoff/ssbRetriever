ckan.module('query_form', function($, _) {
    return {
        initialize: function() {
	    	var showingQuery = false;
		var packageID = document.getElementById('resource-edit').action
		console.log("pkg_name: " +packageID)
		var doReplace = false;
		if(packageID.indexOf("new_resource")){
			doReplace = true;
		}
	
		document.getElementById('resource-edit').action = packageID;
        	$('#form-toggle').on('click', function() {
			if(showingQuery){
				document.getElementById('field-query-url').value = "";
				document.getElementById('field-query-text').value = "";
				document.getElementById('field-image-url').value = " ";
				$('#query-inputs').hide();
				$('.image-upload').show();
				document.getElementById('resource-edit').action = packageID;
				showingQuery = false;
			} else {
				$('#field_image_url').val("query");
				document.getElementById('field-image-url').value = " ";
				$('#query-inputs').show();
				$('.image-upload').hide();
				if(doReplace){
					document.getElementById('resource-edit').action = packageID.replace("new_resource/","new?id=");
				}
				console.log(document.getElementById('resource-edit').action)
				showingQuery = true;
			}
        	});
    	}
    };
});
