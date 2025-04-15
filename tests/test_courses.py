from playwright.sync_api import sync_playwright, expect, Page
import pytest

from pages.courses_list_page import CoursesListPage
from pages.create_course_page import CreateCoursePage
from pages.dashboard_page import DashboardPage


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(courses_list_page: CoursesListPage, dashboard_page_with_state: DashboardPage):
    courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

    dashboard_page_with_state.navbar.check_visible('username')
    dashboard_page_with_state.sidebar.check_visible()

    courses_list_page.check_visible_courses_title()

    courses_list_page.check_visible_create_course_button()

    courses_list_page.check_visible_empty_view()


@pytest.mark.courses
@pytest.mark.regression
def test_create_course(courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
    create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
    create_course_page.check_visible_create_course_title()
    create_course_page.check_disabled_create_course_button()
    create_course_page.check_visible_image_preview_empty_view()
    create_course_page.check_visible_image_upload_view()
    create_course_page.check_visible_create_course_form(
        '',
        '',
        '',
        '0',
        '0'
    )
    create_course_page.check_visible_exercises_title()
    create_course_page.check_visible_create_exercise_button()
    create_course_page.check_visible_exercises_empty_view()
    create_course_page.upload_preview_image('./testdata/files/image.png')
    create_course_page.check_visible_image_upload_view()
    create_course_page.fill_create_course_form(
        'Playwright',
        '2 weeks',
        'Playwright',
        '100',
        '10'
    )
    create_course_page.click_create_course_button()

    courses_list_page.check_visible_courses_title()
    courses_list_page.check_visible_create_course_button()
    courses_list_page.check_visible_course_card(
        0,
        'Playwright',
        '100',
        '10',
        '2 weeks'
    )
