import hashlib

from .file_utils import FileUtils


class Criptography:

    def __init__(self):
        self.file_utils = FileUtils()
        self.letters = 'abcdefghijklmnopqrstuvwxyz'

    def word_correspondence(self, word, key):
        if not word.isalpha():
            return word
        update_key = key % len(self.letters)
        index = self.letters.find(word) - update_key
        return self.letters[index]

    def descriptography(self):
        data = self.file_utils.read()
        text = data['cifrado'].lower()
        key = data['numero_casas']
        new_text = ''

        for i, word in enumerate(text):
            new_word = self.word_correspondence(
                word, key)
            new_text += new_word

        data['decifrado'] = new_text
        self.file_utils.write(data)

    def resume_sha1(self):
        data = self.file_utils.read()
        resume = hashlib.sha1(
                (data['decifrado']).encode('utf-8')
            ).hexdigest()
        data['resumo_criptografico'] = resume
        self.file_utils.write(data)
