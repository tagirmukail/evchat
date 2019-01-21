function init_datetime() {
    $('#datetimepicker6').datetimepicker({
        locale: 'ru',
        format: 'DD/MM/YYYY HH:mm',
        sideBySide: true
    });
    $('.glyphicon-remove').click(function() {
        $('#datetimepicker6').data("DateTimePicker").clear();
    });
}

function init() {

    var myMap;

    myMap = new ymaps.Map("map", {
        center: [55.76, 37.64],
        zoom: 13,
        controls: []
    });

    myMap.behaviors.disable('scrollZoom');
    myMap.controls.add("zoomControl", {
        position: { top: 15, left: 15 }
    });

    var searchControl = new ymaps.control.SearchControl({
        options: {
            provider: 'yandex#map'
        }
    });

    myMap.controls.add(searchControl);

    searchControl.events.add('resultselect', function(e) {

        var results = searchControl.getResultsArray();
        var selected = e.get('index');
        var result = results[selected];
        $('#id_place').val(result.properties.get('text'));
        $('#place_label').html("Your selected place: " + $('#id_place').val());
    })
}

$(document).ready(function() {

    init_datetime();
    ymaps.ready(init);

});