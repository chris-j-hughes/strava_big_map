<html>
  <head>
    <title>Mapping Strava</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.3.2/dist/leaflet.css" integrity="sha512-Rksm5RenBEKSKFjgI3a41vrjkw4EVPlJ3+OiI65vTjIdo9brlAacEuKOiQ5OFh7cOI1bkDwLqdLw3Zg0cRJAAQ==" crossorigin=""/>
    <script src="https://unpkg.com/leaflet@1.3.2/dist/leaflet.js" integrity="sha512-2fA79E27MOeBgLjmBrtAgM/20clVSV8vJERaW/EcnnWCVGwQRazzKtQS1kIusCZv1PtaQxosDZZ0F1Oastl55w==" crossorigin=""></script>
	<script type="text/javascript" src="https://rawgit.com/jieter/Leaflet.encoded/master/Polyline.encoded.js"></script>
  </head>

  <body>
    <div id="map" style="width: 100%; height: 100%"></div>
   
    <script>
    
    function getColor(perc) {
		p = (perc - 2) / (4 - 2);
		val = 100 +( (360-100) * p)
		return ('hsl(' + val + ', 100%, 50%');
	}
    
	var map = L.map('map').setView([53.48, -2.28], 13);
	var base = L.tileLayer(
		'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
		maxZoom: 18,
	}).addTo(map);
	var baserelief = L.tileLayer(
		'https://tiles.wmflabs.org/hillshading/{z}/{x}/{y}.png', {
		maxZoom: 18,
	}).addTo(map);
	var basedark = L.tileLayer(
		'https://cartodb-basemaps-{s}.global.ssl.fastly.net/dark_all/{z}/{x}/{y}.png', {
		maxZoom: 18,
	}).addTo(map);

	var encodedRoutes = [<?php
		$handle = fopen("polylines.csv", "r");
		$line = fgets($handle);
		if ($handle) {
			while (($line = fgets($handle)) !== false) {
				$pieces = explode(",", $line);
				if ($pieces[2] != "Swim" && $pieces[1] != "")
				echo "[\"" . addslashes(rtrim($pieces[1])) . "\", \"" . rtrim($pieces[3]) . "\", \"" . rtrim($pieces[4]) . "\", \"" . rtrim($pieces[2]) . "\", \"" . rtrim($pieces[0]) . "\"],\n";
			}
			fclose($handle);
		} 
	?>]
	
	layerGroupRun = L.layerGroup();
	layerGroupRide = L.layerGroup();
	for (let encoded of encodedRoutes) {
		var coordinates = L.Polyline.fromEncoded(encoded[0]).getLatLngs();
		if (encoded[3] == "Run"){
			L.polyline(coordinates,{
				color: getColor(encoded[2]),
				weight: 2,
				opacity: .7,
				lineJoin: 'round'
			})
			.on('mouseover', function (e) {
				e.target.setStyle({
				  color: 'red',
				  weight: 8,
				  opacity: 1
				});
			})
			.on('mouseout', function (e) {
				e.target.setStyle({
				  color: getColor(encoded[2]),
				  weight: 2,
				  opacity: .7
				});
			})
			.on('click', function (e) {
				window.open('https://www.strava.com/activities/'+ encoded[4], '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes');
			})
			.addTo(layerGroupRun);
		}
		else if (encoded[3] == "Ride"){
			L.polyline(coordinates,{
				color: getColor(encoded[2]),
				weight: 2,
				opacity: .7,
				lineJoin: 'round'
			}).on('mouseover', function (e) {
				e.target.setStyle({
				  color: 'red',
				  weight: 8,
				  opacity: 1
				});
			})
			.on('mouseout', function (e) {
				e.target.setStyle({
				  color: getColor(encoded[2]),
				  weight: 2,
				  opacity: .7
				});
			})
			.on('click', function (e) {
				window.open('https://www.strava.com/activities/'+ encoded[4], '_blank', 'location=yes,height=570,width=520,scrollbars=yes,status=yes');
			})
			.addTo(layerGroupRide);
		}
	}    
	layerGroupRun.addTo(map)
	layerGroupRide.addTo(map)

	var baseMaps = {
		"Base": base,
		"Relief": baserelief,
		"Dark": basedark
	};
	var overlayMaps = {
		"Runs (Polyline)": layerGroupRun,
		"Rides (Polyline)": layerGroupRide,
	};
	L.control.layers(baseMaps, overlayMaps).addTo(map);
    </script>
  </body>
</html>