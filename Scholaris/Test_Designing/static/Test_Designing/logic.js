$(function(){
    var current_qs =1;
    var qs_attempted;
    var percentage = 0;

    //calling clear ans function
    $("#cls_ans").click(clear_ans);

    //console.log($(".qs-text").value);
    progress(percentage);
    $('.carousel').carousel('pause');

    //function for previous button
    $("#prev").click(function(){
        if(get_current() != 1) {
            $('.carousel').carousel('prev');
            mrev(0);
        }
    });

    //function for next button
    $("#next").click(function(){
        if(get_current() != 10) {
            $('.carousel').carousel('next');
            mrev(0);
        }
        else{
            window.alert("Its the last question! Please click Submit");
        }
    });

    //function for review & next
    $("#mnext").click(function(){
        if(get_current() != 10) {
            mrev(1);//adding class review
            $('.carousel').carousel('next');
            mrev(0);
        }
        else{
            window.alert("Its the last question!Can't review");
        }
    });


    //to start the slide-show
    $(".carousel-item").first().addClass("active");


    $('input[type=radio]').click(function () {
        qs_attempted = $(':radio:checked');
        console.log(qs_attempted);
        //console.log(number);
        percentage = (qs_attempted.length *100)/number;
        progress(percentage);
        console.log(percentage);
    })


});

//function to shuffle
$.fn.shuffle = function() {

			var allElems = this.get(),
				getRandom = function(max) {
					return Math.floor(Math.random() * max);
				},
				shuffled = $.map(allElems, function(){
					var random = getRandom(allElems.length),
						randEl = $(allElems[random]).clone(true)[0];
					allElems.splice(random, 1);
					return randEl;
			   });

			this.each(function(i){
				$(this).replaceWith($(shuffled[i]));
			});

			return $(shuffled);

};

//function to add question numbers for each question
function text_qs(num){
    for(i=1;i<=num;i++){
        txt = "Question "+i;
        $(".qs-text").eq(i-1).text(txt);
    }
}

//functions to question panel
function change_qs(i){
    $('.carousel').carousel(i);
    mrev(0);
    return false;
}


function prog_count() {
    qs_attempted = $(':radio:checked');
    console.log(qs_attempted);
}


function create(num){
    var x =0,y=0;
    for(var i=0;i<num;i++){
        btn = "<button onclick='change_qs("+i+");return false'  class='btn btn-info rounded-circle mx-2 py-2 px-3 my-2' id='btn-"+i+"'>"+(i+1)+"</button>";
        $("#qs-panel").append(btn);
        if((i+1)%4 == 0){
            $("#use").append("<br>")
        }
    }
}



var x = setInterval(function(){
	timer_no--;

	var minutes = Math.floor(timer_no /60);
	var seconds = Math.floor(timer_no % 60);

	document.getElementById("demo1").innerHTML = minutes + "m " + seconds + "s ";

	if ( timer_no< 0) {
        clearInterval(x);
        $("#examform").submit();
        console.log("exam form submitted");
        document.getElementById("demo1").innerHTML = "EXPIRED";
    }
},1000);


 function progress(num) {
    $(".progress-bar").css("width",''+num+'%');
	$(".progress-bar").text(num+"%");
}

//function to clear ans
function clear_ans(){
     /*
     x = $(".active .qs-text").text();
     var i =x[x.length - 1];
     $('input[name=qs-'+i+']').attr('checked',false);
     */
     var i= get_current();
     $('input[name=qs-'+questions_order[i-1]+']').prop("checked",false);
}

//shuffuling options
function shuff(num){
     for(var i=1;i<=num;i++){
        $('div#shuffle-'+i+' label').shuffle();
    }
}

//function to get current positon of div
function get_current(){
     x = $(".active .qs-text").text();
     var i = x.split(" ")
     return parseInt(i[1])
}

//adding or removing class for review
//pass 1 for adding review,pass 0 for removing review
function mrev(x) {
     var i = get_current();
     console.log(i);
     if(x == 1) {
         $('#btn-' + (i - 1)).addClass('review');
         $('#btn-' + (i - 1)).removeClass('btn-info');
     }
     if(x == 0){
         $('#btn-' + (i - 1)).addClass('btn-info');
         $('#btn-' + (i - 1)).removeClass('review');
     }
}