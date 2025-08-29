chip_id_input = input("Please enter chipID: ")

def encrypt_string(chip_id):
    if not chip_id:
        return ""

    try:
        if len(chip_id) < 8:
            return chip_id

        result = (hex((int(chip_id[-8:], 16) + 514365010) ^ 174714)[2:])[-6:]

        return result

    except Exception as e:
        print(f"encrypt error: {e}")
        return ""

print(f"Anykeymeister made this code for you: {encrypt_string(chip_id_input)}")
