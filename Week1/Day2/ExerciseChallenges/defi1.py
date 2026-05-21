import sys


def index_letters(word: str) -> dict:
    """Return a dictionary mapping each character in word to a list of its indices.

    Examples:
    >>> index_letters('dodo')
    {'d': [0, 2], 'o': [1, 3]}
    >>> index_letters('froggy')
    {'f': [0], 'r': [1], 'o': [2], 'g': [3, 4], 'y': [5]}
    """
    result = {}
    for i, ch in enumerate(word):
        if ch in result:
            result[ch].append(i)
        else:
            result[ch] = [i]
    return result


def main():
    # If run with the 'test' argument, run example tests and exit.
    if len(sys.argv) > 1 and sys.argv[1] == 'test':
        examples = ['dodo', 'froggy', 'raisins']
        for w in examples:
            print(f"{w} -> {index_letters(w)}")
        return

    word = input('Enter a word: ')
    print(index_letters(word))


if __name__ == '__main__':
    main()
