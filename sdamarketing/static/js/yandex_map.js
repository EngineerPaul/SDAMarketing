// Function for Yandex maps
ymaps.ready(function(){
    mapexMap = new ymaps.Map("mapexMap", {
        center: [59.902347,30.27668],
        zoom: 15
    });
    mapexMap.setType("yandex#map");
    var mapexMapControls = "mapTools".split(',');
    for(var i = 0; i < mapexMapControls.length; i++){
        mapexMap.controls.add(mapexMapControls[i]);
    }
    mapexMap.geoObjects.add(new ymaps.Placemark([59.902691,30.277474], {"iconContent":"\u041c\u0430\u0440\u043a\u0435\u0442\u0438\u043d\u0433\u043e\u0432\u043e\u0435 \u0430\u0433\u0435\u043d\u0442\u0441\u0442\u0432\u043e SDA","balloonContentBody":"","balloonContentHeader":"\u041c\u0430\u0440\u043a\u0435\u0442\u0438\u043d\u0433\u043e\u0432\u043e\u0435 \u0430\u0433\u0435\u043d\u0442\u0441\u0442\u0432\u043e SDA"}, {"preset":"twirl#redStretchyIcon"}));

});