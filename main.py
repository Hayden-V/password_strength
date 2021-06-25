# A strong password contains at least eight characters, contains both uppercase and lowercase,
# one special character as [!@#$%^&*], and has at least one digit.

import re


# Check that the password contain at least eight characters.
def length_test(a_password):
    a_compile = re.compile(r'^.{8,}$')
    return a_compile.search(a_password)


# Check that the password contains uppercase and lowercase.
def case_test(a_password):
    a_compile = re.compile(r'(?=.*[a-z])(?=.*[A-Z])')  # This uses positive look ahead, very useful.
    return a_compile.search(a_password)


# Check that the password contains at least one digit.
def digit_test(a_password):
    a_compile = re.compile((r'(?=.*\d)'))  # This uses positive look ahead, very useful.
    return a_compile.search(a_password)


# Check that the password contains a special character.
def special_char_test(a_password):
    a_compile = re.compile((r'(?=.[*!@#\$%\^&\*])'))  # This uses positive look ahead, very useful.
    return a_compile.search(a_password)


# Run all strength tests.
def master_test(a_password):
    if length_test(a_password):
        print('The password passed the length test.')
    else:
        print("The password is too short. It needs to be at least eight characters.")
    if case_test(a_password):
        print('The password passed the case test.')
    else:
        print("The password needs at least one uppercase and lowercase letter.")
    if digit_test(a_password):
        print("The password passed the digit test")
    else:
        print("The password needs at least one digit.")
    if special_char_test(a_password):
        print("The password passed the special character test.")
    else:
        print("The password needs at least one special character.")
    if length_test(a_password) and case_test(a_password) and digit_test(a_password) and special_char_test(a_password):
        return "Your password is strong!"
    else:
        return "Your password is not strong enough!"


# Change the test password here.
print(master_test('aA345678!'))
