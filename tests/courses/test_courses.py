import pytest
import allure
from tools.allure.tags import AllureTag
from tools.allure.epics import AllureEpic
from tools.allure.features import AllureFeature
from tools.allure.stories import AllureStory
from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage
from pages.dashboard.dashboard_page import DashboardPage
from allure_commons.types import Severity


@pytest.mark.courses
@pytest.mark.regression
@allure.tag(AllureTag.REGRESSION, AllureTag.COURSES)
@allure.epic(AllureEpic.LMS)
@allure.feature(AllureFeature.COURSES)
@allure.story(AllureStory.COURSES)
class TestCourses:
    @allure.title('Check displaying of empty courses list')
    @allure.severity(Severity.NORMAL)
    def test_empty_courses_list(self, courses_list_page: CoursesListPage, dashboard_page_with_state: DashboardPage):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        dashboard_page_with_state.navbar.check_visible('username')
        dashboard_page_with_state.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()

        courses_list_page.check_visible_empty_view()

    @allure.title('Create course')
    @allure.severity(Severity.CRITICAL)
    def test_create_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.create_course_toolbar.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.fill_create_course_form.check_visible(
            title='',
            estimated_time='',
            description='',
            max_score='0',
            min_score='0'
        )
        create_course_page.exercise_toolbar_view.check_visible()
        create_course_page.check_visible_exercises_empty_view()
        create_course_page.exercise_toolbar_view.click_create_exercise_button()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.fill_create_course_form.fill(
            title='Playwright',
            estimated_time='2 weeks',
            description='Playwright',
            max_score='100',
            min_score='10'
        )
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title='Playwright',
            max_score='100',
            min_score='10',
            estimated_time='2 weeks'
        )

    @allure.title('Edit course')
    @allure.severity(Severity.CRITICAL)
    def test_edit_course(self, courses_list_page: CoursesListPage, create_course_page: CreateCoursePage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.fill_create_course_form.fill(
            title='Playwright',
            estimated_time='1 weeks',
            description='Playwright',
            max_score='100',
            min_score='10'
        )
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/image.png')
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.course_view.check_visible(
            0,
            title='Playwright',
            max_score='100',
            min_score='10',
            estimated_time='1 weeks'
        )

        courses_list_page.course_menu.menu_button.click()
        courses_list_page.course_menu.edit_menu_button.click()

        create_course_page.fill_create_course_form.fill(
            title='Playwright 2',
            estimated_time='2 weeks',
            description='Playwright 2',
            max_score='101',
            min_score='11'
        )
        create_course_page.create_course_toolbar.click_create_course_button()

        courses_list_page.course_view.check_visible(
            0,
            title='Playwright 2',
            max_score='101',
            min_score='11',
            estimated_time='2 weeks'
        )
