$(document).ready(function(){
	$("#slider_range_area").slider({
		range: true,
		min: 0,
		max: 500,
		values: [50, 350],
		slide: function(event, ui){
			$("#area_min").val(ui.values[0]);
			$("#area_max").val(ui.values[1]);
		}
	});
	$("#area_min").val($("#slider_range_area").slider("values", 0));
	$("#area_max").val($("#slider_range_area").slider("values", 1));

	$("#slider_range_area_land").slider({
		range: true,
		step: 1000,
		min: 0,
		max: 2000000000,
		values: [50, 1500000000],
		slide: function(event, ui){
			$("#area_min_land").val(ui.values[0]);
			$("#area_max_land").val(ui.values[1]);
		}
	});
	$("#area_min_land").val($("#slider_range_area_land").slider("values", 0));
	$("#area_max_land").val($("#slider_range_area_land").slider("values", 1));

	$("#slider_range_area_commercial").slider({
		range: true,
		min: 0,
		max: 200000,
		values: [50, 150000],
		slide: function(event, ui){
			$("#area_min_commercial").val(ui.values[0]);
			$("#area_max_commercial").val(ui.values[1]);
		}
	});
	$("#area_min_commercial").val($("#slider_range_area_commercial").slider("values", 0));
	$("#area_max_commercial").val($("#slider_range_area_commercial").slider("values", 1));

	$("#slider_range_area_industry").slider({
		range: true,
		min: 0,
		max: 200000,
		values: [50, 150000],
		slide: function(event, ui){
			$("#area_min_industry").val(ui.values[0]);
			$("#area_max_industry").val(ui.values[1]);
		}
	});
	$("#area_min_industry").val($("#slider_range_area_industry").slider("values", 0));
	$("#area_max_industry").val($("#slider_range_area_industry").slider("values", 1));

	$("#slider_range_price").slider({
		range: true,
		step: 1000,
		min: 0,
		max: 2000000000,
		values: [7000000, 1500000000],
		slide: function(event, ui){
			$("#price_min").val(ui.values[0]);
			$("#price_max").val(ui.values[1]);
		}
	});
	$("#price_min").val($("#slider_range_price").slider("values", 0));
	$("#price_max").val($("#slider_range_price").slider("values", 1));

	var currentYear = new Date();

	$("#slider_range_constYear").slider({
		range: true,
		min: 1900,
		max: currentYear.getFullYear(),
		values: [1950, 2016],
		slide: function(event, ui){
			$("#constYear_min").val(ui.values[0]);
			$("#constYear_max").val(ui.values[1]);
		}
	});
	$("#constYear_min").val($("#slider_range_constYear").slider("values", 0));
	$("#constYear_max").val($("#slider_range_constYear").slider("values", 1));

	$("#slider_range_manufYear").slider({
		range: true,
		min: 1900,
		max: currentYear.getFullYear(),
		values: [1950, 2016],
		slide: function(event, ui){
			$("#manufYear_min").val(ui.values[0]);
			$("#manufYear_max").val(ui.values[1]);
		}
	});
	$("#manufYear_min").val($("#slider_range_manufYear").slider("values", 0));
	$("#manufYear_max").val($("#slider_range_manufYear").slider("values", 1));
});