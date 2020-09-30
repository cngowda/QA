import pytest

def pytest_addoption(parser):
    parser.addoption("--CSP_HOST", action="store", help="csp host")
    parser.addoption("--CSP_USER", action="store", help="csp user")
    parser.addoption("--iteration", action="store", help="csp host")
    parser.addoption("--refresh", action="store", help="csp user")

@pytest.fixture
def params(request):
    params = {}
    params['CSP_HOST'] = request.config.getoption('--CSP_HOST')
    params['CSP_USER'] = request.config.getoption('--CSP_USER')
    params['iteration'] = request.config.getoption('--iteration')
    params['refresh'] = request.config.getoption('--refresh')
    if params['CSP_HOST'] is None or params['CSP_USER'] is None:
        pytest.skip()
    return params