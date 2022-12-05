from selene.support.shared import browser
import pytest
from selene import be, have
import os


def test_automation_practice_form(practice_form_open_browser):
    #проверка валидации
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have._not_.exact_text('Student Registration Form'))
    browser.element('#firstName').should(be.blank).type('Test')
    browser.element('#lastName').should(be.blank).type('User')
    browser.element('#userEmail').should(be.blank).type('testuser2@gmail.com')
    #проверка работы всех трех кнопок
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[for="gender-radio-2"]').click()
    browser.element('[for="gender-radio-3"]').click()
    browser.element('#userNumber').type('1111111111')
    browser.element('#userNumber').matching(have.exact_text('1111111111'))
    browser.element('#userNumber').clear()
    browser.element('#userNumber').type('22222222223')
    #проверка, что более 10 символов не ввести
    browser.element('#userNumber').matching(have.exact_text('2222222222'))
    #автоматический выбор даты и заодно проверка на указание даты рождения в будущем
    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__navigation--previous').click()
    browser.element('.react-datepicker__navigation--next').click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('[value="11"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('[value="2022"]').click()
    browser.element('.react-datepicker__day--010').click()
    browser.element('#subjectsInput').should(be.blank).type('History').press_enter()
    browser.element('#subjectsInput').should(be.blank).type('Computer Science').press_enter()
    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('#uploadPicture').set_value(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir, 'example.png')))
    browser.element('#currentAddress').should(be.blank).type('Test text')
    # выбор через кнопки
    browser.element('#state').click()
    browser.element('#react-select-3-input').press_enter()
    browser.element('#city').click()
    browser.element('#react-select-4-input').press_enter()
    #выбор через текст
    browser.element('#react-select-3-input').should(be.blank).type('Haryana').press_enter()
    browser.element('#react-select-4-input').should(be.blank).type('Karnal').press_enter()
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.element('.table').should(have.text('Test' and 'User' and 'testuser2@gmail.com' and 'Other' and '2222222222' and '10 December,2022' and 'History, Computer Science' and 'Sports, Reading, Music' and 'example.png' and 'Test text' and 'Haryana' and 'Karnal'))