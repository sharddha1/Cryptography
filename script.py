def vigenere_decrypt(ciphertext, key):
    key_len = len(key)
    decrypted_text = ""
    for i in range(len(ciphertext)):
        if ciphertext[i].isalpha():
            key_shift = ord(key[i % key_len].lower()) - ord('a')
            if ciphertext[i].isupper():
                decrypted_char = chr((ord(ciphertext[i]) - key_shift - 65) % 26 + 65)
            else:
                decrypted_char = chr((ord(ciphertext[i]) - key_shift - 97) % 26 + 97)
            decrypted_text += decrypted_char
        else:
            decrypted_text += ciphertext[i]
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
