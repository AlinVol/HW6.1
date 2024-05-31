import string


def letters_between(input_str):
    start_letter, end_letter = input_str.split('-')

    start_index = string.ascii_letters.index(start_letter)
    end_index = string.ascii_letters.index(end_letter)

    return string.ascii_letters[start_index:end_index + 1]


input_str = input("Enter two letters separated by a hyphen: ")
result = letters_between(input_str)
print(result)
