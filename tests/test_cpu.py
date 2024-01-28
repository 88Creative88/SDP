import pytest
from conftest import client
@pytest.mark.unit
def test_cpu(mocker):
    from app import cpu_temp
    mocker.patch('flaskr.view.cpu.Hardware.get_cpu_temp', return_value=33.0)
    temperature = cpu_temp()
    assert '33.0' == temperature
    #assert cpu_temp() == 'CPU Temperature'

@pytest.mark.api
def test_cpu_error(mocker, client):
    from app import cpu_temp_error
    mocker.patch('flaskr.view.cpu.Hardware.get_cpu_temp', return_value=33.0)
    response = client.get('/cpu/temp/error')
    assert b'33.0' == response.data
    #assert cpu_temp_error() == 'CPU Temperature Error'

