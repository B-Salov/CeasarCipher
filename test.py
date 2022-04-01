import string


class CeasarCipher:

    def __init__(self, phrase, shift, alphabet):
        self.phrase = phrase
        self.shift = shift
        self.alphabet = alphabet

    def encode(self):
        shift_alphabet = tuple(map(lambda x: x[self.shift:] + x[:self.shift],
                                   self.alphabet))

        original_alphabet = ''.join(self.alphabet)
        shifted_alphabet = ''.join(shift_alphabet)

        result = str.maketrans(original_alphabet, shifted_alphabet)

        return self.phrase.translate(result)

    def decode(self):
        pass


def _main():
    phrase = str(input('Your phrase --> '))
    # options = int(input(' 1 - Encode \n 2 - Decode\n --> '))

    shift = int(input('Shift --> '))

    alphabet = [string.ascii_letters, string.punctuation]

    ceasar = CeasarCipher(phrase, shift, alphabet)
    result = ceasar.encode()

    print(result)


if __name__ == '__main__':
    _main()
