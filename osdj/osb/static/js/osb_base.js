$(document).ready(function(){
	checkMessageNumber();
	setInterval("checkMessageNumber()",5000)
});

function checkMessageNumber(){
	$.get("/osb/checkMessageNumber/",
		function(data){
			if(data > 0){
				$("#messageCount").html(data);	
			}
			else{
				$("#messageCount").fadeOut();	
			}
	});
}
