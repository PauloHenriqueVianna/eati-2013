
var latlng = new google.maps.LatLng(-27.347984,-53.425537);
var point = new google.maps.LatLng(-27.389754,-53.431654);

var myOptions = {
  zoom: 11,
  center: latlng,
  mapTypeControl: true,
  mapTypeId: google.maps.MapTypeId.ROADMAP
};
var map = new google.maps.Map(document.getElementById("mapa"), myOptions);
var contentString = '<div class="row-fluid"><div class="span3"><img src="../assets/img/logo-eati-maps.png"></div><div class="span9"><h2><b>Encontro Anual de Tecnologia da Informação</b></h2></div></div>';
var infowindow = new google.maps.InfoWindow({
    content: contentString
});
var marker = new google.maps.Marker({
	    position: point,
	    map: map,
	    title: 'Colégio Agrícola de Frederico Westphalen'
	  	});
marker.setIcon('../assets/img/computers.png');
infowindow.open(map,marker);
google.maps.event.addListener(marker, 'click', function() {
	infowindow.open(map,marker);
});