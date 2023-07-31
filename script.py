def vigenere_decrypt(ciphertext, key):
    key_len = len(key)
    decrypted_text = ""
    key_index = 0
    for char in ciphertext:
        if char.isalpha():
            key_shift = ord(key[key_index % key_len].lower()) - ord('a')
            if char.isupper():
                decrypted_char = chr((ord(char) - key_shift - 65) % 26 + 65)
            else:
                decrypted_char = chr((ord(char) - key_shift - 97) % 26 + 97)
            decrypted_text += decrypted_char
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text

def vigenere_attack(ciphertext, max_key_length=12):
    for key_length in range(1, max_key_length + 1):
        substrings = [''] * key_length
        for i, char in enumerate(ciphertext):
            if char.isalpha():
                substrings[i % key_length] += char.lower()

        potential_keys = []
        for substring in substrings:
            letter_frequencies = [0] * 26
            for letter in substring:
                letter_frequencies[ord(letter) - ord('a')] += 1
            most_common_letter_index = letter_frequencies.index(max(letter_frequencies))
            key_shift = (most_common_letter_index - (ord('e') - ord('a'))) % 26
            potential_keys.append(chr(key_shift + ord('a')))

        key = ''.join(potential_keys)
        decrypted_text = vigenere_decrypt(ciphertext, key)
        print(f"Key length: {key_length}, Key: {key}, Decrypted text: {decrypted_text}")

if __name__ == "__main__":
    ciphertext = input("Enter the Vigenère-encrypted ciphertext: ")
    vigenere_attack(ciphertext)

