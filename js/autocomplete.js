//adds autocomplete functionality to gene search bar
window.onload=function() {

   $("#search_term").autocomplete({

      //gets possible values by searching database
      source: function(request, response) {

	//queries database
	$.ajax({

		url: "./autocomplete_te.cgi",
		type: 'get',
		dataType: "json",
		data: {
		   search_term: request.term
		},
		success: function(data) {
		   response(data);
		}
	});

      },
	
      //the minimum number of characters needed to trigger autocomplete
      minLength: 2,

      //writes the clicked option into the search bar
      select: function(event, ui) {
		$("#search_term").val(ui.item.label);
      },
   });

}
