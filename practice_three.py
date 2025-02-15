class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        result = []
        for letter in original_text:
            if letter.lower() in self.alphabet:
                index = self.alphabet.index(letter.lower())
                new_index = (index + shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                result.append(letter)
        return ''.join(result).lower()

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        result = []
        for letter in cipher_text:
            if letter.lower() in self.alphabet:  # Lower the letter for correct comparison
                # Lower the letter to find the index
                index = self.alphabet.index(letter.lower())
                new_index = (index - shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                result.append(letter)
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Уфмьпт фиёав ё ьмшфтёдсстр ёмзи. Одкицхг, сдх фдххофяпм!,',
    shift=4
))
