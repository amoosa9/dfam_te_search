//adds autocomplete functionality to gene search bar
window.onload=function() {

   $("#search_term").autocomplete({
      //gets possible values by searching database
      source: "./autocomplete_te.cgi",
	
      //the minimum number of characters needed to trigger autocomplete
      minLength: 2,

      //searches if autocomplete option is clicked
      select: function(event, ui) {
		$("#search_term").val(ui.item.label);
		runSearch();
      },
   });

}
