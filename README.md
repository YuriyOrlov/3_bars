# Ближайшие бары

Скрипт работает с файлом JSON взятым с портала открытых данных правительства города Москвы.

Ссылка: http://data.mos.ru/opendata/7710881420-bary

Он позволяет:
* выбрать самый большой бар
* выбрать самый мальнький бар
* выбрать ближайший бар при введении координат с клавиатуры из консоли

------------------------------
This script works with JSON file taken from open data portal of Moscow city government.
It lets you to do the following:
* choose the biggest bar in Moscow
* choose the smallest bar in Moscow
* choose the nearest bar to your current location if you enter your coordinates from keyboard in console

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```#!bash

$ python bars.py # possibly requires call of python3 executive instead of just python

The biggest bar is: Спорт бар «Красная машина»

The smallest bar is: Бар в Деловом центре Яуза

Enter your coordinates ("longitude;latitude") using semicolon(";") as a splitter> 55.678386;37.561052

The closest bar is: Спорт-бар «Торнадо»


```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
