
var latlng = new google.maps.LatLng(-27.389754,-53.431654);

var myOptions = {
  zoom: 8,
  center: latlng,
  mapTypeControl: true,
  mapTypeId: google.maps.MapTypeId.ROADMAP
};
var map = new google.maps.Map(document.getElementById("mapa"), myOptions);
var contentString = '<b>Colégio Agrícola de Frederico Westphalen</b><br>Encontro Anual de Tecnologia da Informação';
var infowindow = new google.maps.InfoWindow({
    content: contentString
});
var marker = new google.maps.Marker({
	    position: latlng,
	    map: map,
	    title: 'Colégio Agrícola de Frederico Westphalen'
	  	});
google.maps.event.addListener(marker, 'click', function() {
	infowindow.open(map,marker);
});
