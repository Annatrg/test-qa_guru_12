import allure
from selene import have, command
import os


@allure.title("Successful fill form")
def test_successful(setup_browser):
    browser = setup_browser

    with allure.step("Open registrations form"):
        browser.open("https://demoqa.com/automation-practice-form")
        browser.element(".practice-form-wrapper").should(have.text("Student Registration Form"))
        browser.driver.execute_script("$('footer').remove()")
        browser.driver.execute_script("$('#fixedban').remove()")

    with allure.step("Fill form"):
        browser.element('#firstName').type('Anna')
        browser.element('#lastName').type('Torgova')
        browser.element('#userEmail').type('test_anna@mail.ru')
        browser.element('[for="gender-radio-2"]').click()
        browser.element('#userNumber').type('79990001122')
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').click().element('option[value="10"]').click()
        browser.element('.react-datepicker__year-select').click().element('option[value="1996"]').click()
        browser.element('.react-datepicker__day--026').click()
        browser.element("#subjectsInput").type("Arts").press_enter()
        browser.element('[for="hobbies-checkbox-1"]').click()
        browser.element('[for="hobbies-checkbox-2"]').click()
        browser.element('[for="hobbies-checkbox-3"]').click()

        browser.element('[id="stateCity-label"]').perform(command.js.scroll_into_view)
        browser.element('#uploadPicture').send_keys(os.path.abspath('picture/test.jpg'))

        browser.element('#currentAddress').type('Saint-Petersburg')
        browser.element('#react-select-3-input').type('NCR').click().press_enter()
        browser.element('#react-select-4-input').type('Delhi').click().press_enter()
        # Создание анкеты
        browser.element('#submit').click()

    with allure.step("Check form results"):
        browser.element("#example-modal-sizes-title-lg").should(have.text("Thanks for submitting the form"))
