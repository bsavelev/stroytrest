$(function(){
	var $map = $("#metro-map"),
			$map_img_nr = $map.find(".metro-map__img_normal"),
			$map_img_bl = $map.find(".metro-map__img_blur"),
			$map_stantion = $map.find(".metro-map__stantions .item"),
			$metro_list = $(".metro-stantions-list"),
			$container = $(".metro-select-stantions"),
			aClass = "active",
			$clear = $(".metro-map-clear");
	$map_stantion.on("click",function(){
		var id = $(this).index(),
				$sel = $metro_list.find("option").eq(id);
				blur = false;
		if ($sel.prop("selected")==true) {
			$sel.prop("selected", false);
			$container.find("#"+id).remove();
		} else {
			$sel.prop("selected", true);
			$container.append("<span id='"+id+"'>"+$(this).html()+"</span>");
		}
		$metro_list.find("option").each(function(){
			if ($(this).prop("selected")==true) {
				blur=true;
			}
		});
		if (blur==true) {
			$map.addClass(aClass);
			$(".metroLink").html("Выбранные станции:");
		} else {
			$map.removeClass(aClass);
			$(".metroLink").html("Выбрать станцию метро");
		}
		$(this).toggleClass(aClass);
	});
	$clear.on("click",function(){
		$metro_list.find("option").prop("selected", false);
		$map_stantion.removeClass(aClass);
		$map.removeClass(aClass);
		$(".metroLink").html("Выбрать станцию метро");
		$container.find("span").remove();
	});
});