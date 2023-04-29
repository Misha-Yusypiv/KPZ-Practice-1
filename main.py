import re
import platform

def palindrom(*args):
    result = []
    for word in args:
        if word == word[::-1]:
            result.append(word)
    return result

def validate_ip(ip_address):
    pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
    if re.match(pattern, ip_address):
        return True
    else:
        return False

def get_os():
    os_name = platform.system()
    if os_name == 'Darwin':
        return 'Mac'
    elif os_name == 'Windows':
        return 'Windows'
    elif os_name == 'Linux':
        return 'Linux'

print(palindrom("Око", "Дід"))
ip_address = "192.168.0.1"

print(validate_ip(ip_address))
print(get_os())




