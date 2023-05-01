import pytest
from pythonProject1.prime_num_generator import prime_num_generator
from pythonProject1.validator_ip import validate_ip
from pythonProject1.palindrom import palindrom

def test_prime_num_generator():
    print(prime_num_generator(12))
    assert prime_num_generator(12) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    print(prime_num_generator(101)[-1])
    assert prime_num_generator(101)[-1] == 547

def test_palindrom():
    print(palindrom("hello"))
    assert palindrom("hello") == False
    print(palindrom(""))
    assert palindrom("") == False
    print(palindrom("Око"))
    assert palindrom("Око") == True
    print(palindrom("Дід"))
    assert palindrom("Дід") == True

def test_validate_ip():
    print(validate_ip("192.168.0.1"))
    assert validate_ip("192.168.0.1") == True
    print(validate_ip(""))
    assert validate_ip("") == False
    print(validate_ip("192.168.0.1."))
    assert validate_ip("192.168.0.1.") == False
    print(validate_ip("192.168.0"))
    assert validate_ip("192.168.0") == False

def test_get_os():
    print(get_os())
    assert get_os() in ["Windows", "Linux", "MacOS"]

if __name__ == "__main__":
    pytest.main()
