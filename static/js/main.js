

$(document).ready(function() {
  console.log("Mapssss Sanity Check");

  let map;

  // Make the map
  function initMap() {
    map = new google.maps.Map(document.getElementById("map"), {
      center: { lat: 37.7659475, lng: -122.4394986 },
      zoom: 12.7
    });
  }

  initMap();

  // Get the sightings
  $.ajax({
    url: '/get-sightings',
    method: "GET",
    success: function(data) {
      console.log(data);

      for (let i = 0; i < data.sightings.length; i++) {
        // Get the sighting and separate coordinates into a list
        const coords = data.sightings[i].location.split(',')
        console.log(coords)

        lat = parseFloat(coords[0]);
        lng = parseFloat(coords[1]);
        console.log(lat, lng);

        myLatLng = {
            lat: lat,
            lng: lng
          };

        // Make a sighting marker
        let marker = new google.maps.Marker({
          position: myLatLng,
          map: map,
          title: data.sightings[i].bird,
        });
        // An InfoWindow displays content (usually text or images) in a popup window above the map, at a given location.
        let infowindow = new google.maps.InfoWindow({
          // Content has to be a string, not an array!!
          content: `${data.sightings[i].bird_name}, ${data.sightings[i].address}, ${data.sightings[i].observer_name}`
        });
        marker.addListener("click", function() {
          infowindow.open(map, marker);
        });
      }
    }
  });
});
















// This was under the for statement at line 26
        // let time = (
        //   (Date.now() - data.sightings[i].properties.time) /
        //   60 /
        //   60 /
        //   1000
        // ).toFixed(2);
        // $("#info").append(
        //   `<p>${data.sightings[i].properties.title} / ${time} hours ago</p>`
        // );


// under line 44
 //   icon: {
        //     url: "images/earthquake.png",
        //     scaledSize: { height: 40, width: 40 }
        //   }



// under line 23 
    // debugger;
      // data.sightings[0].properties.title