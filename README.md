# Ближайшие бары

Этот скрипт может найти **ближайщий**, **наименьший**, **наибольший** бар.

Данные берутся из **JSON** файла [Списка московских баров.](https://data.mos.ru/opendata/7710881420-bary) 

Скрипт **запрашивает GPS координаты** пользователя для поиска ближайщего бара.

# Как запустить

Скрипт требует для своей работы установленного интерпретатора Python версии 3.5

Запуск на Linux:

```bash

$ python bars.py  <path to file> # possibly requires call of python3 executive instead of just python

```

**Пример** ответа в консоль:

```bash
The BIGGEST bar is:
    Name: Спорт бар «Красная машина»
    Number of seats: 450
    Coordinates: 37.638228501070095, 55.70111462948684
The SMALLEST bar is:
    Name: БАР. СОКИ
    Number of seats: 0
    Coordinates: 37.35805920566864, 55.84614475898795
The CLOSEST bar is:
    Name: Грэйс Бар
    Number of seats: 68
    Coordinates: 37.632064484372663, 55.756834594680008
```

Запуск на Windows происходит аналогично.

# Цели проекта

Код создан в учебных целях. В рамках учебного курса по веб-разработке - [DEVMAN.org](https://devman.org)
