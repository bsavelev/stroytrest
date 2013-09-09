$( document ).ready( function(){

	$( '#tab_nav a' ).click(function() {
		var tab_id = $(this).parent().index();
		tabClick( tab_id );
	});
	function tabClick( tab_id ) {
		if ( tab_id != $( '#tab_nav li.active' ).index() ) {
			$( '#tab_form .tab, #tab_result .tab, #tab_nav li' ).removeClass( 'active' );
			$( '#tab_nav a' ).parent().eq( tab_id ).addClass( 'active' );
			$( '#tab_form .tab' ).eq( tab_id ).addClass( 'active' );
			$( '#tab_result .tab' ).eq( tab_id ).addClass( 'active' );
		}
	}

	$( "#slider_range_price" ).slider({
		range: true,
		min: 0,
		max: 99999,
		values: [ 10000, 50000 ],
		slide: function( event, ui ) {
			$( "#price_from" ).val( ui.values[ 0 ] );
			$( "#price_to" ).val( ui.values[ 1 ] );
		}
	});
	$( "#price_from" ).val( $( "#slider_range_price" ).slider( "values", 0 ) );
	$( "#price_to" ).val( $( "#slider_range_price" ).slider( "values", 1 ) );

	$( "#slider_range_price1" ).slider({
		range: true,
		min: 0,
		max: 99999,
		values: [ 10000, 50000 ],
		slide: function( event, ui ) {
			$( "#price_from1" ).val( ui.values[ 0 ] );
			$( "#price_to1" ).val( ui.values[ 1 ] );
		}
	});
	$( "#price_from1" ).val( $( "#slider_range_price1" ).slider( "values", 0 ) );
	$( "#price_to1" ).val( $( "#slider_range_price1" ).slider( "values", 1 ) );

	$( "#slider_range_price2" ).slider({
		range: true,
		min: 0,
		max: 99999,
		values: [ 10000, 50000 ],
		slide: function( event, ui ) {
			$( "#price_from2" ).val( ui.values[ 0 ] );
			$( "#price_to2" ).val( ui.values[ 1 ] );
		}
	});
	$( "#price_from2" ).val( $( "#slider_range_price2" ).slider( "values", 0 ) );
	$( "#price_to2" ).val( $( "#slider_range_price2" ).slider( "values", 1 ) );

	$( "#slider_range_price3" ).slider({
		range: true,
		min: 0,
		max: 99999,
		values: [ 10000, 50000 ],
		slide: function( event, ui ) {
			$( "#price_from3" ).val( ui.values[ 0 ] );
			$( "#price_to3" ).val( ui.values[ 1 ] );
		}
	});
	$( "#price_from3" ).val( $( "#slider_range_price3" ).slider( "values", 0 ) );
	$( "#price_to3" ).val( $( "#slider_range_price3" ).slider( "values", 1 ) );

	$( "#slider_range_price4" ).slider({
		range: true,
		min: 0,
		max: 99999,
		values: [ 10000, 50000 ],
		slide: function( event, ui ) {
			$( "#price_from4" ).val( ui.values[ 0 ] );
			$( "#price_to4" ).val( ui.values[ 1 ] );
		}
	});
	$( "#price_from4" ).val( $( "#slider_range_price4" ).slider( "values", 0 ) );
	$( "#price_to4" ).val( $( "#slider_range_price4" ).slider( "values", 1 ) );

	$( "#slider_range_price5" ).slider({
		range: true,
		min: 0,
		max: 99999,
		values: [ 10000, 50000 ],
		slide: function( event, ui ) {
			$( "#price_from5" ).val( ui.values[ 0 ] );
			$( "#price_to5" ).val( ui.values[ 1 ] );
		}
	});
	$( "#price_from5" ).val( $( "#slider_range_price5" ).slider( "values", 0 ) );
	$( "#price_to5" ).val( $( "#slider_range_price5" ).slider( "values", 1 ) );

	$( "#slider_range_price6" ).slider({
		range: true,
		min: 0,
		max: 99999,
		values: [ 10000, 50000 ],
		slide: function( event, ui ) {
			$( "#price_from6" ).val( ui.values[ 0 ] );
			$( "#price_to6" ).val( ui.values[ 1 ] );
		}
	});
	$( "#price_from6" ).val( $( "#slider_range_price6" ).slider( "values", 0 ) );
	$( "#price_to6" ).val( $( "#slider_range_price6" ).slider( "values", 1 ) );

	$( "#slider_range_price7" ).slider({
		range: true,
		min: 0,
		max: 99999,
		values: [ 10000, 50000 ],
		slide: function( event, ui ) {
			$( "#price_from7" ).val( ui.values[ 0 ] );
			$( "#price_to7" ).val( ui.values[ 1 ] );
		}
	});
	$( "#price_from7" ).val( $( "#slider_range_price7" ).slider( "values", 0 ) );
	$( "#price_to7" ).val( $( "#slider_range_price7" ).slider( "values", 1 ) );

	$( "#slider_range_area" ).slider({
		range: true,
		min: 10,
		max: 1000,
		values: [ 100, 400 ],
		slide: function( event, ui ) {
			$( "#area_from" ).val( ui.values[ 0 ] );
			$( "#area_to" ).val( ui.values[ 1 ] );
		}
	});
	$( "#area_from" ).val( $( "#slider_range_area" ).slider( "values", 0 ) );
	$( "#area_to" ).val( $( "#slider_range_area" ).slider( "values", 1 ) );


	$( "#slider_range_years" ).slider({
		range: true,
		min: 2013,
		max: 2020,
		values: [ 2014, 2016 ],
		slide: function( event, ui ) {
			$( "#years_from" ).val( ui.values[ 0 ] );
			$( "#years_to" ).val( ui.values[ 1 ] );
		}
	});
	$( "#years_from" ).val( $( "#slider_range_years" ).slider( "values", 0 ) );
	$( "#years_to" ).val( $( "#slider_range_years" ).slider( "values", 1 ) );
});