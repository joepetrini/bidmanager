function search(){
	var url = '/search?';

	//Text;
	if ((q = $('#query').val()) != ''){
		url += 'q=' + htmlEscape(q) + '&';
	}

	//Levels
	url += urlize_checks('levels');

	//Counties
	url += urlize_checks('counties');

	//Categories
	url += urlize_checks('categories');



	//Order by

	//Page

	//Remove last &
	url = url.replace(/\&$/, '');
	//Redirect
	window.location = url;
}

function recheck_from_url(){
	if ((q = getParameterByName("q")) != null){
		$('#query').val(q);
	}

	if ((q = getParameterByName("levels")) != null){
		q.split('-').map(function (e) {
			$('#level_' + e).prop('checked', true);
		});
	}
	if ((q = getParameterByName("counties")) != null){
		q.split('-').map(function (e) {
			$('#county_' + e).prop('checked', true);
		});
	}
	if ((q = getParameterByName("categories")) != null){
		q.split('-').map(function (e) {
			$('#category_' + e).prop('checked', true);
		});
	}
	$('#query').focus();
}

function urlize_checks(div_id){
	var retval = '';
	$('#' + div_id + ' input:checked').each(function(i) {
		if (i == 0){
			retval += div_id + '=';
		}
		retval += this.value + '-'
	});

	if (retval != ''){
		retval = retval.slice(0, - 1);
		retval += '&';
	}
	//retval = (retval == '') ? retval : retval + '&';
	return retval;
}


function htmlEscape(str) {
    return String(str)
            .replace(/&/g, '&amp;')
            .replace(/"/g, '&quot;')
            .replace(/'/g, '&#39;')
            .replace(/</g, '&lt;')
            .replace(/>/g, '&gt;');
}

function htmlUnescape(value){
    return String(value)
        .replace(/&quot;/g, '"')
        .replace(/&#39;/g, "'")
        .replace(/&lt;/g, '<')
        .replace(/&gt;/g, '>')
        .replace(/&amp;/g, '&');
}

function getParameterByName(name) {
    name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
    var regex = new RegExp("[\\?&]" + name + "=([^&#]*)"),
        results = regex.exec(location.search);
    return results == null ? "" : decodeURIComponent(results[1]);
}

$.fn.pressEnter = function(fn) {  

    return this.each(function() {  
        $(this).bind('enterPress', fn);
        $(this).keyup(function(e){
            if(e.keyCode == 13)
            {
              $(this).trigger("enterPress");
            }
        })
    });  
 }; 
