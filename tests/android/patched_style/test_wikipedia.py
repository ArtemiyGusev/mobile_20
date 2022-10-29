from selene import have, be
from selene.support.shared import browser
from allure import step as title

from mobile_tests_lesson_13.model import app


def test_search():
    app.given_opened()

    with title('Check tab explore '):
        browser.element('Search Wikipedia').should(be.visible)

    with title('Check tab saved'):
        browser.element('Saved').tap()
        browser.element('#main_toolbar').element('«Saved»').should(be.visible)

    with title('Check tab search'):
        browser.element('Search').tap()
        browser.element('#history_title').should(have.text('History'))

    with title('Check tab edits'):
        browser.element('Edits').tap()
        browser.element('#main_toolbar').element('«Edits»').should(be.visible)