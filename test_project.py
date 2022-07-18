import pytest
from project import validate_email
from project import file_to_be_sent




def test_validate_email():
    assert validate_email('priya123@gmail.com') == True
    assert validate_email('iampriya') == 'please use correct email'

def test_file_to_be_sent():
    assert file_to_be_sent() == 'C:/Users/kshet/Desktop/daily_progress\\test_file.png'



