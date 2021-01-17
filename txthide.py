
SPACE = " "  # 0
TAB = "\t"  # 1


def str_to_whitespaces(message):
    _message = ""
    for c in message:
        binary_code = format(ord(c), "08b")
        for i in binary_code:
            if i == "0":
                _message += SPACE
            else:
                _message += TAB
    return _message


def whitespaces_to_str(string):
    message = ""
    binary_code = ""
    for i in range(0, len(string), 8):
        c = string[i:i + 8]
        for j in c:
            if j == SPACE:
                binary_code += "0"
            else:
                binary_code += "1"
        message += chr(int(binary_code, 2))

        binary_code = ""
    return message
