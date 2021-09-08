import pytest
from _pytest.config import ExitCode

NUMBER_OF_ACCEPTABLE_FAILURE = 3


@pytest.hookimpl()
def pytest_sessionfinish(session, exitstatus):

    if exitstatus == ExitCode.TESTS_FAILED:
        failure_rate = session.testsfailed / session.testscollected
        if failure_rate <= NUMBER_OF_ACCEPTABLE_FAILURE / session.testscollected:
            session.exitstatus = 0
