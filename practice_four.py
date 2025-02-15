class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        result = []
        for letter in text:
            if letter.lower() in self.alphabet:
                index = self.alphabet.index(letter.lower())
                new_index = (index + shift) % len(self.alphabet) if is_encrypt else (index - shift) % len(self.alphabet)
                result.append(self.alphabet[new_index])
            else:
                result.append(letter)
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Уфмьпт фиёав ё ьмшфтёдсстр ёмзи. Одкицхг, сдх фдххофяпм!,',
    shift=4,
    is_encrypt=False
))
