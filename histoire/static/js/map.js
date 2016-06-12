var map;
var mapDiv = document.getElementById('map');

var satView = document.getElementById('satView');
var EventView = document.getElementById('eventView');
var Year = document.getElementById('year');
var Range = document.getElementById('range');
var Bouton = document.getElementById('bouton');

satView.addEventListener("change", function () {
    setMapOnAll(null);
});

EventView.addEventListener("change", function () {
    var year = Year.value;
    addMarker(year);
    setMapOnAll(map);
});

Bouton.addEventListener("click", function() {
    var year = Range.value;
    Year.value = year;
    if (EventView.checked) {
        addMarker(year);
        setMapOnAll(map);
    }
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
}

function setMapOnAll(map){
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
  }
}

function showValue(newValue) {
    document.getElementById("range").value=newValue;
}



