import pytest
from conftest import client
@pytest.mark.unit
def test_cpu():
    from app import cpu_temp
    assert cpu_temp() == 'CPU Temperature'

@pytest.mark.api
def test_cpu_error():
    from app import cpu_temp_error
    response = client.get('/cpu/temp/error')

    assert cpu_temp_error() == 'CPU Temperature Error'

