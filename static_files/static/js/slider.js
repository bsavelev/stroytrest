(function( $ ){
	$.fn.slides = function( h, s, d ) {

	var SlideSpeed = 700,
		TimeOut = 3000,
		slideNum = 0,
		slideTime;

	var $slides = $( this ).find( ".slide" ),
		$controls = $( this ).find( ".controls" );

	if ( h != null ) {
		$( this ).css({
			"height" : h
		})
	}

	if ( s != null ) {
		SlideSpeed = s;
	}

	if ( d != null ) {
		TimeOut = d;
	}

	$slides.hide().eq(0).show();
	slideCount = $slides.size();

	var animSlide = function(arrow){
		clearTimeout( slideTime );

		$slides.eq( slideNum ).fadeOut( SlideSpeed );

		if(arrow == "next") {
			if( slideNum == (slideCount-1) ) {
				slideNum=0;
			} else{
				slideNum++
			}
		} else if ( arrow == "prew" ) {
			if( slideNum == 0 ){
				slideNum=slideCount-1;
			} else {
				slideNum-=1
			}
		} else {
			slideNum = arrow;
		}

		$slides.eq( slideNum ).fadeIn( SlideSpeed, rotator );
		$controls.find( "span" ).removeClass( "active" );
		$controls.find( "span" ).eq( slideNum ).addClass( "active" );
	}

	var $controlsNum = "";
	$slides.each(function(index) {
		$controlsNum += "<span class='control'>" + index + "</span>";
	});

	$controls.prepend( $controlsNum );
	$controls.find( "span" ).filter( ":first").addClass( "active" );

	$controls.find( "span" ).click(function(){
		var goToNum = parseFloat( $(this).text() );
		animSlide( goToNum );
	});

	var pause = false;
	var rotator = function(){
		if(!pause) {
			slideTime = setTimeout( function(){ animSlide( "next") }, TimeOut );
		}
	}

	$( this ).hover(	
		function(){
			clearTimeout(slideTime);
			pause = true;
		}, function(){
			pause = false;
			rotator();
		});
	rotator();
	};
})( jQuery );




// var $linkArrow = $('<a class="prew" href="#">&lt;</a><a class="next" href="#">&gt;</a>')
// 	.prependTo('.slider-content');		
// 	$('.next').click(function(){
// 		animSlide("next");
// 		return false;
// 		})
// 	$('.prew').click(function(){
// 		animSlide("prew");
// 		return false;
// 		})
