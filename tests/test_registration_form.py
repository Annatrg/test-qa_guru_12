import allure
from selene import have, command
import os


@allure.title("Регистрация")
def test_successful(setup_browser):
    browser = setup_browser

    with allure.step("Открыть страницу регистрации"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Укажите Ваше имя"):
        browser.element('#firstName').type('Anna')
    with allure.step("Укажите Вашу фамилию"):
        browser.element('#lastName').type('Torgova')
    with allure.step("Укажите Вашу электронную почту"):
        browser.element('#userEmail').type('test_anna@mail.ru')
    with allure.step("Укажите Ваш пол"):
        browser.element('[for="gender-radio-2"]').click()
    with allure.step("Укажите Ваш номер телефона"):
        browser.element('#userNumber').type('79990001122')
    with allure.step("Укажите Вашу дату рождения"):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element('option[value="10"]').click()
        browser.element('.react-datepicker__year-select').click().element('option[value="1996"]').click()
        browser.element('.react-datepicker__day--026').click()
    with allure.step("Укажите Ваши хобби"):
        browser.element("#subjectsInput").type("Arts").press_enter()
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-2"]').click()
        browser.element('[for="hobbies-checkbox-3"]').click()
    with allure.step("Загрузите Ваше фото"):
        browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
        browser.element('#uploadPicture').send_keys(os.path.abspath('picture/test.jpg'))
    with allure.step("Укажите Ваш адрес"):
        browser.element('#currentAddress').type('Saint-Petersburg')
        browser.element('#react-select-3-input').type('NCR').click().press_enter()
        browser.element('#react-select-4-input').type('Delhi').click().press_enter()
    with allure.step("Подтверждение создания анкеты"):
        browser.element('#submit').click()

    with allure.step("Проверка результата"):
        browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
        browser.element('.table').all('td:nth-of-type(2)').should(have.texts(
            'Anna Torgova',
            'test_anna@mail.ru',
            'Female',
            '7999000112',
            '26 November,1996',
            'Arts',
            'Sports, Reading, Music',
            'test.jpg',
            'Saint-Petersburg',
            'NCR Delhi'))
