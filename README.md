# final-python

Кинопоиск UI и API тесты - Python
Задача проекта провести проверку модуля поиска (фильм/сериал/персона), возможности авторизации, установки оценки фильму/сериалу, добавление фильма/сериала в необходимую папку на сайте Кинопоиск. Проект состоит из 7 ui тестов и 5 api тестов.
Полезные ссылки:
[https://www.notion.so/1-fef7898d658f442a8679cc6a66f2a24d?pvs=4](https://drive.google.com/file/d/1-22U4imv0VPFE7vDXARQww_Bzxtyfxvp/view?usp=sharing)
Проект содержит папки:
pages - в данной папке находятся файлы с методами страниц сервиса Кинопоиск.

test - в данной папке находятся файлы с UI и API тестами.

api - в данной папке находятся файлы с методами API Кинопоиска.

Проект содержит файлы:
requirements.txt - файл с используемыми зависимостями в проекте. Установить зависимости на тестовый стенд можно командой pip install -r requirements.txt

conftest.py - файлы с фикстурами, используемыми в проекте.

config.json - файл с данными, которые используются для авторизации на сайте (логин и пароль), url адреса для ui и api тестов, содержит также информацию о заголовке и токене, передаваемых в api тестах.

AuthPageKinopoisk.py - содержит методы класса страницы авторизации на сайте.

MainPageKinopoisk.py - содержит методы класса главной страницы сайта, страницы результатов поиска. В данном файле находятся методы: обработка капчи, ввод запроса в модуль поиска, сбор информации по подсказкам к поиску, нажатие нопки поиска, получения информация на странице результата поиска, методы поиска фильма или сериала, персоны и ошибочного (пустого поиска).

FilmSeriesPageKinopoisk.py - файл с методами класса персональной страницы фильма, сериала или персоны. Здесь находятся методы поиска элемента на странице и нажатия на него, нахождение элемента и считывание его текста (и дальнейший его возврат), нахождение кнопок, контроль установленной оценки, установка, изменение и удаление оценки.

UserPageKinopoisk.py - файл с методами класса страницы пользователя. Здесь находятся методы: переход в личный кабинет пользователя, метод позволяющий открыть необходимый раздел в кабинете, метод собирающий информацию в разделе Фильмы и метод для раздела Оценки.

FilmTvSeriesApi.py - содержит методы класса поиска фильма или сериала с использованием Api. Методы поиска фильма/сериала по названию, id, дополнительным полям.

PersonAPi.py - содержит методы класса поиска персоны с использованием Api. Методы поиска персоны по имени и фамилии, id.

test_ui.py - файл с тестами ui. Тесты запускаются командой python -m pytest --alluredir <папка для результатов>. Сформировать отчет allure serve <папка с результатами>.

test_api.py - файл с тестами api. Тесты запускаются командой python -m pytest --alluredir <папка для результатов>. Сформировать отчет allure serve <папка с результатами>.
