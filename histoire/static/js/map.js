var map;
var mapDiv = document.getElementById('map');

/*function CoordMapType(tileSize) {
  this.tileSize = tileSize;
}

CoordMapType.prototype.maxZoom = 19;
CoordMapType.prototype.name = 'Tile #s';
CoordMapType.prototype.alt = 'Tile Coordinate Map Type';

CoordMapType.prototype.getTile = function(coord, zoom, ownerDocument) {
  var div = ownerDocument.createElement('div');
  div.innerHTML = coord;
  div.style.width = this.tileSize.width + 'px';
  div.style.height = this.tileSize.height + 'px';
  div.style.fontSize = '10';
  div.style.borderStyle = 'solid';
  div.style.borderWidth = '1px';
  div.style.borderColor = '#AAAAAA';
  div.style.color = 'white';
  return div;
};*/


/*function initialize() {
    var Latlng = new google.maps.LatLng(49.224,5.4357);    
    
    var mapOptions = {
        zoom: 8,
        center:Latlng,
        streetViewControl: false,
        mapTypeId: google.maps.MapTypeId.SATELLITE
    };
    
    map = new google.maps.Map(mapDiv, mapOptions);
    
}


    /*map.addListener('maptypeid_changed', function() {
        var showStreetViewControl = map.getMapTypeId() !== 'coordinate';
        map.setOptions({
            streetViewControl: showStreetViewControl
        });
    });*/

    //map.overlayMapTypes.insertAt(0, new CoordMapType(new google.maps.Size(256, 256)));
    
    /*google.maps.event.addListener(map, 'click', function(e){
        addMarker(e.latLng, map);
    });*/

/*function setMarker(map){
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
  }
}
    
    /*{% for marker in markers %}
        var image = {
            url:{{ marker.event.image }},
            size: new google.maps.Size(20,32),
            origin: new google.maps.Point(0,0),
            anchor: new google.maps.Point(0,32)
        };
   
        var marker = new google.maps.Marker({
            icon: image,
            position: new google.maps.LatLng({{ marker.latitude }},{{ marker.longitude }}),
            map:map
        });
    {% endfor %}*/
    
    

//google.maps.event.addDomListener(window, 'load', initialize);


var satView = document.getElementById('satView');
var EventView = document.getElementById('eventView');

satView.addEventListener("change", function () {
    setMarker(null);
});

EventView.addEventListener("change", function () {
    setMarker(map);
});



