import string


class CeasarCipher:

    def __init__(self, phrase, shift, alphabet):
        self.phrase = phrase

        shift_alphabet = tuple(map(lambda x: x[shift:] + x[:shift],
                                   alphabet))

        self.original_alphabet = ''.join(alphabet)
        self.shifted_alphabet = ''.join(shift_alphabet)

    def encode(self):
        result = str.maketrans(self.original_alphabet,
                               self.shifted_alphabet)

        return self.phrase.translate(result)

    def decode(self):
        result = str.maketrans(self.shifted_alphabet,
                               self.original_alphabet)

        return self.phrase.translate(result)


def _main():
    phrase = str(input('Your phrase --> '))
    shift = int(input('Shift --> '))
    shift %= 26
    option = int(input(' 1 - Encode \n 2 - Decode\n --> '))

    alphabet = [string.ascii_lowercase, string.ascii_uppercase, string.punctuation]

    ceasar = CeasarCipher(phrase, shift, alphabet)

    if option == 1:
        encode_result = ceasar.encode()
        print(encode_result)
    elif option == 2:
        decode_result = ceasar.decode()
        print(decode_result)
    else:
        print('Incorrect option!')
        exit()


if __name__ == '__main__':
    _main()
