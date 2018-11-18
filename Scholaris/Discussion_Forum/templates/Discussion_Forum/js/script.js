/* =====================Pre Loader===================== */

$(window).on('load', function() { // makes sure that whole site is loaded
	$('#status').delay(100).fadeOut();
	$('#pre-loader').delay(350).fadeOut('slow');
	
});

/*======================counter up=======================*/

$(function () {
	$(".counter").counterUp({
		delay: 10,
		time: 2000
	});
	
});