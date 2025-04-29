from pages.dashboard.dashboard_page import DashboardPage
import pytest


@pytest.mark.dashboard
@pytest.mark.regression
class TestDashboard:
    def test_dashboard_displaying(self, dashboard_page_with_state: DashboardPage):
        dashboard_page_with_state.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/dashboard')
        dashboard_page_with_state.navbar.check_visible('username')
        dashboard_page_with_state.sidebar.check_visible()
        dashboard_page_with_state.dashboard_toolbar.check_visible()
        dashboard_page_with_state.scores_chart.check_visible('Scores')
        dashboard_page_with_state.courses_chart.check_visible('Courses')
        dashboard_page_with_state.students_chart.check_visible('Students')
        dashboard_page_with_state.activities_chart.check_visible('Activities')
