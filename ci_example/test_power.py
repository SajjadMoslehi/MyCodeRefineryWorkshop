# The file name must start from test_ so that the CI can recognize the test file to run.
# The function name must start from test_ so that the CI cna recognize the test file to run.

from file_power import power

def test_power():
    assert power(3, 3) == 27
