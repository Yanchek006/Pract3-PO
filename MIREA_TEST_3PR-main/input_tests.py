from input import get_city

import mock
import time

import io
import sys

from unittest.mock import patch

# run TDD on get_city() function, simulating user input

@patch('builtins.input', side_effect=['Москва'])
def test_get_city_valid(mock_input):
    assert get_city() == ('Москва', 0.0)

@patch('sys.stdout', new_callable=io.StringIO)
@patch('builtins.input', side_effect=['Moscow', 'Санкт-Петербург', 'Санкт-Петербург'])
def test_get_city_invalid(mock_input, mock_stdout):
    get_city()

    assert mock_stdout.getvalue() == 'Некорректный ввод. \n'
    
    assert get_city() == ('Санкт-Петербург', 0.0)

