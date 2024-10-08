import allure
import json

with open("config.json", "r") as config_file:
    config = json.load(config_file)

base_url_ui = config.get("base_url_ui")
auth_credentials = config.get("auth_credentials")


@allure.feature("Авторизация на сайте.")
@allure.title("Тест авторизации пользователя.")
@allure.description("Авторизуемся на сайте используя входные данные.")
@allure.id(1)
@allure.severity("Blocker")
def test_auth(auth_page):
    auth_page.user_auth(auth_credentials["username"], auth_credentials["password"])
    with allure.step(
        "Проверяем вернулись ли мы на главную страницу после авторизации."
    ):
        expected_url = base_url_ui
        actual_url = auth_page._driver.current_url
        assert actual_url.startswith(expected_url)


@allure.feature("Модуль поиска.")
@allure.title("Тест на поиск фильма или сериала.")
@allure.description("Выполняем поиск фильма или сериала согласно полученным данным.")
@allure.id(2)
@allure.severity("Blocker")
def test_search_film_tv_series(main_page):
    film_tv_series = "Гарри Поттер"
    film_name_search_list, film_name_result_search, film_name_personal_page = (
        main_page.search_film_or_tv_series(film_tv_series)
    )
    with allure.step(
        "Проверяем, что переданное название фильма совпадает с названием выводимым в подсказках к модулю поиска, на странице результата поиска, на персональной странице фильма."
    ):
        assert film_tv_series in film_name_search_list[0]
        assert film_name_result_search.startswith(film_tv_series)
        assert film_name_personal_page.startswith(film_tv_series)


@allure.feature("Модуль поиска.")
@allure.title("Тест на поиск персоны.")
@allure.description("Выполняем поиск персоны согласно полученным данным.")
@allure.id(3)
@allure.severity("Blocker")
def test_search_person(main_page):
    person_info = "Александр Петров"
    person_info_search_list, person_info_result_search, person_info_private_page = (
        main_page.search_person(person_info)
    )
    with allure.step(
        "Проверяем, что переданные фамилия и имя персоны совпадают с данными выводимыми в подсказках к модулю поиска, на странице результата поиска, на личной странице персоны."
    ):
        assert person_info in person_info_search_list[0]
        assert person_info_result_search == person_info
        assert person_info_private_page == person_info


@allure.feature("Модуль поиска.")
@allure.title("Тест поиск по несуществующему названию.")
@allure.description(
    "Выполняем поиск по несуществующему названию, проверяем корректность выдачи информационного сообщения."
)
@allure.id(4)
@allure.severity("Normal")
def test_empty_search_info_message(main_page):
    search_info = "no book such term"
    message = "К сожалению, по вашему запросу ничего не найдено..."
    get_message = main_page.empty_search(search_info)
    with allure.step(
        "Проверяем, что считанное информационное сообщение идентично шаблону."
    ):
        assert get_message == message


@allure.feature("Установка оценки.")
@allure.title("Тест на установку оценки фильму или сериалу.")
@allure.description(
    "Авторизуемся, выполняем поиск фильма или сериала, устанавливаем оценку."
)
@allure.id(5)
@allure.severity("Blocker")
def test_set_rating_for_film_or_tv_series(auth_page, main_page, personal_page):
    # Авторизация пользователя
    auth_page.user_auth(auth_credentials["username"], auth_credentials["password"])
    
    # Поиск фильма или сериала
    film_tv_series = "Артур, ты король"
    film_name_search_list, film_name_result_search, film_name_personal_page = (
        main_page.search_film_or_tv_series(film_tv_series)
    )
    
    # Установка первой оценки
    first_value = 3
    personal_page.set_rating(first_value)
    control_first = personal_page.control_vote()
    
    # Проверка первой оценки
    assert str(first_value) == control_first, f"Ожидалось значение: {first_value}, получено: {control_first}"
    
    # Установка второй оценки
    second_value = 10
    personal_page.change_rating(second_value)
    control_second = personal_page.control_vote()
    
    # Проверка второй оценки
    assert str(second_value) == control_second, f"Ожидалось значение: {second_value}, получено: {control_second}"
    
    # Удаление оценки и проверка текста кнопки
    button_text = "Оценить фильм"
    deleted_rating_button_text = personal_page.delete_rating()
    assert deleted_rating_button_text == button_text, f"Ожидалось текст кнопки: {button_text}, получено: {deleted_rating_button_text}"
