import requests
import js2py
from requests_html import HTML
#
# req = ('https://static-maps.yandex.ru/1.x/?l=map&pl=37.656577,55.741176,37.656748,55.741419,37.655131,55.741814,37.658257,55.742524,37.659811,55.743066,37.659667,55.743233,37.659551,55.743603,37.659775,55.743928,37.662398,55.745281')
# print(req)
#
# array = '55.683058,37.547867,55.683223000000005,37.548097999999996,55.683223000000005,37.548097999999996,55.683179,37.548196999999995,55.68285,37.54893499999999,55.682586,37.54952899999999,55.682528,37.549659999999996,55.682451,37.54983299999999,55.682451,37.54983299999999,55.68224,37.549530999999995,55.68224,37.549530999999995,55.682185,37.54965299999999,55.682447999999994,37.550045999999995,55.683305999999995,37.551328999999996,55.683389999999996,37.551452999999995,55.683552,37.551694,55.683715,37.551939,55.683959,37.552234,55.684054,37.552347,55.684139,37.552451999999995,55.684278,37.552623,55.685005,37.553512999999995,55.685483,37.554097,55.685615,37.554255999999995,55.685783,37.554458999999994,55.686704,37.55557699999999,55.687234,37.556228999999995,55.687259999999995,37.556262,55.687946,37.557086,55.688362,37.557586,55.688429,37.557665,55.689391,37.558873,55.689474,37.558975,55.69,37.559604,55.690576,37.560293,55.691273,37.561127,55.691506000000004,37.561409,55.691574,37.561505999999994,55.691610000000004,37.561564,55.691673,37.561660999999994,55.691937,37.56211199999999,55.691937,37.56211199999999,55.691996,37.56193599999999,55.692047,37.561821999999985,55.692122000000005,37.56166799999998,55.69228700000001,37.561354999999985,55.69273600000001,37.560560999999986,55.69339500000001,37.55938699999999,55.69349000000001,37.55921499999999,55.69426600000001,37.55788599999999,55.694305000000014,37.557816999999986,55.69445500000001,37.55759899999999,55.694516000000014,37.55751899999999,55.694718000000016,37.55725399999999,55.694873000000015,37.557053999999994,55.695065000000014,37.55676799999999,55.695065000000014,37.55676799999999,55.694594000000016,37.555961999999994,55.69450600000002,37.555806999999994,55.69419300000002,37.555251999999996,55.69354500000002,37.554103999999995,55.69310000000002,37.55329999999999,55.69310000000002,37.55329999999999,55.69314600000002,37.55322099999999,55.69411800000002,37.551528999999995,55.69417300000002,37.551432999999996,55.69417300000002,37.551432999999996,55.69443400000002,37.551883999999994,55.69443400000002,37.551883999999994,55.69447400000002,37.551812999999996,55.69465100000002,37.551500999999995,55.69500300000002,37.550903999999996,55.69500300000002,37.550903999999996,55.69505400000002,37.550999999999995,55.69520300000002,37.55128199999999,55.69541600000002,37.55168799999999,55.695623000000026,37.55206999999999,55.695623000000026,37.55206999999999,55.69569500000003,37.55193599999999,55.69590700000003,37.55154699999999'
# array = array.split(',')
# out = []
# for i, _ in enumerate(array):
#     if i % 2 == 0:
#         out.extend(array[i: i + 2][::-1])
# print(','.join(out))
html = HTML(html='<script src="https://api-maps.yandex.ru/2.1/?apikey=577a0e84-44cd-4ad9-ba64-975e632e29a5&lang=ru_RU" type="text/javascript"></script>')
js = """
ymaps.ready(function () {
    var myMap = new ymaps.Map('map', {
        center: [55.751574, 37.573856],
        zoom: 9,
        controls: []
    });

    // Создание экземпляра маршрута.
    var multiRoute = new ymaps.multiRouter.MultiRoute({
        // Точки маршрута.
        // Обязательное поле.
        referencePoints: [
            'ул. Вавилова, 68, к. 2, Москва, 119261',
            'Университетский пр., 5, Москва, 119296'
        ]
    }, {
      // Автоматически устанавливать границы карты так,
      // чтобы маршрут был виден целиком.
      boundsAutoApply: true
});

    // Добавление маршрута на карту.
    myMap.geoObjects.add(multiRoute);

    // Подписка на событие готовности маршрута.
    multiRoute.model.events.add('requestsuccess', function() {
        // Получение ссылки на активный маршрут.
        var activeRoute = multiRoute.getActiveRoute();
        // Получение коллекции путей активного маршрута.
        var activeRoutePaths = activeRoute.getPaths();
        // Проход по коллекции путей.
        activeRoutePaths.each(function(path) {
            var path = '' + path.properties.get("coordinates");
            console.log("Время прохождения пути: " + path.properties.get("duration").text);
        });
    });
    // Добавление маршрута на карту.
    myMap.geoObjects.add(multiRoute);
    return path

});
"""
val = html.render(script=js, reload=False)
print(val)