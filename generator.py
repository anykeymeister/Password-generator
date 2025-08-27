mCryptonInt = 514365010
chip_id_input = input("Please enter chipID: ")

def encrypt_string(chip_id):
    if not chip_id:
        return ""

    try:
        print(f"encrypt deviceID from setting: {chip_id}")

        if len(chip_id) < 8:
            return chip_id

        substring = chip_id[-8:]
        numeric_value = int(substring, 16) + mCryptonInt
        encrypted_value = numeric_value ^ 174714
        result = hex(encrypted_value)[2:]  # Convert to hex and remove '0x' prefix

        if len(result) > 6:
            result = result[-6:]

        print(f"encrypt result: {result}")
        return result

    except Exception as e:
        print(f"encrypt error: {e}")
        return ""


encrypted = encrypt_string(chip_id_input)
print(f"Anykeymeister made this for you: {encrypted}")