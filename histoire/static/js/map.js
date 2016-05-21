var map;
var mapDiv = document.getElementById('map');

var satView = document.getElementById('satView');
var EventView = document.getElementById('eventView');

satView.addEventListener("change", function () {
    setMapOnAll(null);
});

EventView.addEventListener("change", function () {
    setMapOnAll(map);
});


function initialize() {
    var Latlng = new google.maps.LatLng(49.224,5.4357);    
    
    var mapOptions = {
        zoom: 8,
        center:Latlng,
        streetViewControl: false,
        mapTypeId: google.maps.MapTypeId.SATELLITE
    };
    
    map = new google.maps.Map(mapDiv, mapOptions);
    
    addMarker();
}

function setMapOnAll(map){
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
  }
}



