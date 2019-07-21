// Execute JavaScript on page load
var location_data;

window.onload = function() {
navigator.geolocation.getCurrentPosition(function(location) {
    var latitude = location.coords.latitude;
    var longitude = location.coords.longitude;
     console.log(longitude);
    location_data = {"latitude": location.coords.latitude, "longitude": location.coords.longitude};
    console.log(location_data)
});    
document.getElementById("theButton").onclick = function() {
    doWork()
};

}

function doWork() {

    console.log("LOCATION DATA", location_data)
    $.post("receiver", {"location_data": location_data}, function(){
    });
    // stop link reloading the page
    event.preventDefault();
    }



$(function() {
    // Initialize phone number text input plugin
    $('#phoneNumber').intlTelInput({
        responsiveDropdown: true,
        autoFormat: true,
        utilsScript: '/static/js/libphonenumber/src/utils.js'
    });
        // setup the button click

    // Intercept form submission and submit the form with ajax
    $('#contactForm').on('submit', function(e) {
        // Prevent submit event from bubbling and automatically
        // submitting the form

        e.preventDefault();

        // Call our ajax endpoint on the server to initialize the
        // phone call
        $.ajax({
            url: '/call',
            method: 'POST',
            dataType: 'json',
            data: {
                phoneNumber: $('#phoneNumber').val()
            }
        }).done(function(data) {
            // The JSON sent back from the server will contain
            // a success message
            alert(data.message);
        }).fail(function(error) {
            alert(JSON.stringify(error));
        });
    });

   /* var location_data
    navigator.geolocation.getCurrentPosition(function(location) {
        var latitude = location.coords.latitude;
        var longitude = location.coords.longitude;
        console.log(latitude);
        console.log(longitude);
        console.log("hellow");
        location_data = {"latitude": location.coords.latitude, "longitude": location.coords.longitude};
    });

    $('#theButton').on('click', function(e) {
        e.preventDefault();
        console.log(location_data)
        $.ajax({
            url: '/receiver',
            method: 'POST',
            data: {
                locationData: location_data
            }
        }).done(function(data) {
            // The JSON sent back from the server will contain
            // a success message
            alert(data.message);
        }).fail(function(error) {
            alert(JSON.stringify(error));
        }); 

    });*/
});
